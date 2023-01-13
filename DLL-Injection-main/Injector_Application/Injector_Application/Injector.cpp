#include "Injector.h"

BOOL CSRInjector::InjectDll(DWORD dwPid, char* szDllPath)
{
	DWORD   dwMemSize;
	HANDLE  hProc;
	LPVOID  lpRemoteMem, lpLoadLibrary;
	BOOL    bRet = FALSE;

	//Step.1 Attach this Process to the running process
	if((hProc = OpenProcess(PROCESS_ALL_ACCESS, FALSE, dwPid)) != NULL)
	{
		dwMemSize = strlen(szDllPath);
		//Step.2 Allocate Memory within the process
		if((lpRemoteMem = VirtualAllocEx(hProc, NULL, dwMemSize, MEM_COMMIT, PAGE_READWRITE)) != NULL)
			//Step.3 Copy the DLL or the DLL Path into the processes memory and determine appropriate memory addresses
			if(WriteProcessMemory(hProc, lpRemoteMem, szDllPath, dwMemSize, NULL))
			{
				lpLoadLibrary = GetProcAddress(GetModuleHandleA("kernel32.dll"), "LoadLibraryA");

				//Step.4 Instruct the process to Execute your DLL
				if(CreateRemoteThread(hProc, NULL, 0, (LPTHREAD_START_ROUTINE)lpLoadLibrary, lpRemoteMem, 0, NULL) != NULL)
				{
					bRet = TRUE;
				}
			}
	}
	CloseHandle(hProc);

	return bRet;
}
