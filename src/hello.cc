#include <napi.h>
#include <Plum2/Plum2.h>
using namespace Napi;

namespace demo
{
    String method(const CallbackInfo &info)
    {

        return String::New(info.Env(), hello());
    }

    Object initialize(Env env, Object exports)
    {
        exports.Set("hello", Function::New(env, method));
        return exports;
    }

    NODE_API_MODULE(NODE_GYP_MODULE_NAME, initialize)
} // namespace demo
