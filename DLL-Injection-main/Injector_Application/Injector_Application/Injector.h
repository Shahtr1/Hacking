#include <Windows.h>

class CSRInjector
{
public:
	BOOL InjectDll(DWORD dwPid, char* szDllPath);
};