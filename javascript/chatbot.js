const openai = require('openai');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// replace with your API key
const apiKey = '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';

// replace with the ID of your OpenAI model
const modelId = 'YOUR_MODEL_ID';

openai.apiKey = apiKey;

rl.question('What is your name? ', (name) => {
  console.log(`Hello, ${name}! How can I assist you?`);
  rl.on('line', (input) => {
    openai.completions.create({
      engine: 'text-davinci-002',
      prompt: input,
      maxTokens: 150,
      n: 1,
      stop: '\n',
      temperature: 0.7
    }).then((response) => {
      console.log(response.choices[0].text);
    }).catch((err) => {
      console.log(err);
    });
  });
});
