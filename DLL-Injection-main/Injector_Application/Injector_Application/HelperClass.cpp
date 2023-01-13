#include "HelperClass.h"

TCHAR* CSRHelperClass::BrowseFolder()
{
    TCHAR path[MAX_PATH];

    BROWSEINFO bi = { 0 };
    bi.lpszTitle  = _T("Choose DLL Folder");
    bi.ulFlags    = BIF_RETURNONLYFSDIRS | BIF_NEWDIALOGSTYLE;

    LPITEMIDLIST pidl = SHBrowseForFolder ( &bi );

    if ( pidl != 0 )
    {
        //get the name of the folder and put it in path
        SHGetPathFromIDList ( pidl, path );

        //free memory used
        IMalloc * imalloc = 0;
        if ( SUCCEEDED( SHGetMalloc ( &imalloc )) )
        {
            imalloc->Free ( pidl );
            imalloc->Release ( );
        }
		return path;
    }
	else
	{
		return nullptr;
	}
}

DWORD CSRHelperClass::GetProcessIdByName(LPCTSTR lpcszProc)
{
    HANDLE          hSnap;
    PROCESSENTRY32  peProc;
    DWORD           dwRet = -1;

    if((hSnap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)) != INVALID_HANDLE_VALUE)
    {
        peProc.dwSize = sizeof(PROCESSENTRY32);
        if(Process32First(hSnap, &peProc))
            while(Process32Next(hSnap, &peProc))
                if(!lstrcmp(lpcszProc, peProc.szExeFile))
                    dwRet = peProc.th32ProcessID;
    }
    CloseHandle(hSnap);

    return dwRet;
}

LPCTSTR CSRHelperClass::SzToLPCTSTR(char* szString)
{
    LPTSTR  lpszRet;
    size_t  size = strlen(szString)+1;

    lpszRet = (LPTSTR)malloc(MAX_PATH);
    mbstowcs_s(NULL, lpszRet, size, szString, _TRUNCATE);

    return lpszRet;
}

void CSRHelperClass::WaitForProcessToAppear(LPCTSTR lpcszProc, DWORD dwDelay)
{
	HANDLE          hSnap;
	PROCESSENTRY32  peProc;
	BOOL            bAppeared = FALSE;

	while(!bAppeared)
	{
		if((hSnap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)) != INVALID_HANDLE_VALUE)
		{
			peProc.dwSize = sizeof(PROCESSENTRY32);
			if(Process32First(hSnap, &peProc))
				while(Process32Next(hSnap, &peProc) && !bAppeared)
					if(!lstrcmp(lpcszProc, peProc.szExeFile))
						bAppeared = TRUE;
		}
		CloseHandle(hSnap);
		Sleep(dwDelay);
	}
}
