#include <Windows.h>
#include <Python.h>
int main()
{
    // Load the Python interpreter library
    HINSTANCE hInstance = LoadLibrary("python27.dll");

    if (hInstance != NULL)
    {
        Py_Initialize();

        // Call the Python script
        PyRun_SimpleString("import voiceerecog_module \nvoic ");

        Py_Finalize();
    }

    return 0;
}
