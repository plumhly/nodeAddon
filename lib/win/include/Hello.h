#pragma once

#ifndef HELLO_H
#define HELLO_H

// ���Ҫ�ڴ˴�Ԥ����ı�ͷ
#include "framework.h"

#endif //HELLO_H

#ifdef IMPORT_DLL
#else 
#define IMPORT_DLL extern "C" _declspec(dllimport)
#endif

IMPORT_DLL PCHAR hello();