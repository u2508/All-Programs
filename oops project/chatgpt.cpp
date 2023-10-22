#include <iostream>
#include <curl/curl.h>
#include <nlohmann/json.hpp>
using json = nlohmann::json;

static size_t WriteCallback(void *contents, size_t size, size_t nmemb, void *userp) {
    ((std::string*)userp)->append((char*)contents, size * nmemb);
    return size * nmemb;
}

int main() {
    // Prompt user for input message
    std::string input_msg;
    std::cout << "Enter your message: ";
    std::getline(std::cin, input_msg);

    // Send API request to ChatGPT
    CURL *curl;
    CURLcode res;
    std::string response_str;
    curl_global_init(CURL_GLOBAL_ALL);
    curl = curl_easy_init();
    if (curl) {
        std::string request_url = "https://api.openai.com/v1/engines/davinci-codex/completions";
        std::string auth_header = "Authorization: Bearer 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"; // Replace <API_KEY> with your OpenAI API key
        std::string input_json = "{\"prompt\": \"" + input_msg + "\", \"max_tokens\": 60, \"temperature\": 0.5, \"n\": 1, \"stop\": \"\\n\"}";
        struct curl_slist *headers = NULL;
        headers = curl_slist_append(headers, auth_header.c_str());
        headers = curl_slist_append(headers, "Content-Type: application/json");
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
        curl_easy_setopt(curl, CURLOPT_URL, request_url.c_str());
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, input_json.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response_str);
        res = curl_easy_perform(curl);
        if (res != CURLE_OK) {
            std::cerr << "Failed to get response from API: " << curl_easy_strerror(res) << std::endl;
        }
        curl_slist_free_all(headers);
        curl_easy_cleanup(curl);
    }
    curl_global_cleanup();

    // Parse API response and display output
    json response_json = json::parse(response_str);
    std::string output_msg = response_json["choices"][0]["text"];
    std::cout << "ChatGPT: " << output_msg << std::endl;

    return 0;
}
