#pragma once

#ifndef HELLO_H
#define HELLO_H

// 添加要在此处预编译的标头
#include "framework.h"

#endif //HELLO_H

#ifdef IMPORT_DLL
#else 
#define IMPORT_DLL extern "C" _declspec(dllimport)
#endif

IMPORT_DLL PCHAR hello();