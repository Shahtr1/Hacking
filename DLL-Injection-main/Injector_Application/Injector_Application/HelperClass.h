#include "CommonHeaders.h"

class CSRHelperClass
{
public:
	TCHAR* BrowseFolder();

	DWORD GetProcessIdByName(LPCTSTR lpcszProc);

	LPCTSTR SzToLPCTSTR(char* szString);
	
	void WaitForProcessToAppear(LPCTSTR lpcszProc, DWORD dwDelay);
};