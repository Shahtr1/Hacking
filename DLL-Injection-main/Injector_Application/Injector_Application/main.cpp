#include "HelperClass.h"
#include "Injector.h"

#define MAX_PATH 1000
#define MAX_NUM_OF_TRIES 3
#define WAIT_FOR_PROCESS_TO_APPEAR 1
using namespace std;
int		giNumOfTries = 0;

int main()
{
	CSRHelperClass* phelperOb = new CSRHelperClass;
	char    szProc[MAX_PATH], szDll[MAX_PATH];
	char*   szDllPath = (char*)malloc(MAX_PATH);
	LPTSTR  lpszProc = NULL;
	DWORD pid = -1;

	for(;;)
	{
		if(-1 == pid)
		{
			cout<<"\n***************************************************************************";
			cout << "\n\nPlease Enter the Victim Process name where you want to Inject your DLL: ";
			cin >> szProc;
			strcat_s(szProc, MAX_PATH, ".exe");

			pid = phelperOb->GetProcessIdByName(phelperOb->SzToLPCTSTR(szProc));

			if(-1 == pid)
			{
				std::cout<<"\nProcess is not running. Please try again."<<std::endl;
				if(++giNumOfTries < MAX_NUM_OF_TRIES)
				{
					cout<<"\nPlease make sure that the Process is running. \nTries Left:"<<MAX_NUM_OF_TRIES - giNumOfTries;
					continue;
				}
				else
				{
					std::cout<<"\nExceeded number of Tries. Quitting the Application."<<std::endl;
					break;
				}
			}

			giNumOfTries = 0;
		}
		cout << "\nPlease Enter the DLL name to be Injected: ";
		cin >> szDll;
		strcat_s(szDll, MAX_PATH, ".dll");

		TCHAR* c_wFolderLocation = phelperOb->BrowseFolder();
		if(!c_wFolderLocation)
		{
			cout<<"\nAbnormal Termination. Exiting.";
			break;
		}

		char c_szFolderLocation[MAX_PATH];
		wcstombs(c_szFolderLocation, c_wFolderLocation, wcslen(c_wFolderLocation) + 1);

		szDllPath = c_szFolderLocation;
		strcat_s(szDllPath, MAX_PATH, "\\");
		strcat_s(szDllPath, MAX_PATH, szDll);
		
		if(!std::ifstream(szDllPath))
		{
			if(++giNumOfTries < MAX_NUM_OF_TRIES)
			{
				cout<<"\nCould not locate the DLL. Please Try Again.\nTries Left: "<<MAX_NUM_OF_TRIES - giNumOfTries;
				continue;
			}
			else
			{
				cout<<"\nCould not Locate the DLL. Exceeded number of Tries. Exiting.";
				break;
			}
		}
		else
		{
			giNumOfTries = 0;
		}
#if WAIT_FOR_PROCESS_TO_APPEAR
		cout << "\nWaiting for process: " << szDllPath << " " << szDll << endl;
		phelperOb->WaitForProcessToAppear(phelperOb->SzToLPCTSTR(szProc), 100);
#endif
		CSRInjector obInjector;
		if(obInjector.InjectDll(pid, szDllPath))
		{
			cout << "Injection Succeeded!" << endl;
		}
		else
		{
			cout << "Injection Failed!" << endl;
		}
		break;
	}

	cout<<"\n****************PRESS ANY KEY TO EXIT******************";
	delete(phelperOb);
	phelperOb = nullptr;
	getch();
	return 0;
}
