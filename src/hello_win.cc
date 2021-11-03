#include <napi.h>
#include <windows.h>
#include <Hello.h>
using namespace Napi;

namespace demo
{
    String method(const CallbackInfo &info)
    {
        //HMODULE t = LoadLibrary((LPCWSTR)"hello.dll");
        //typedef PCHAR(*Hello)();
        //Hello hello = (Hello)GetProcAddress(t, "hello");

        return String::New(info.Env(), hello());
    }

    Object initialize(Env env, Object exports)
    {
        exports.Set("hello", Function::New(env, method));
        return exports;
    }

    NODE_API_MODULE(NODE_GYP_MODULE_NAME, initialize)
} // namespace demo
