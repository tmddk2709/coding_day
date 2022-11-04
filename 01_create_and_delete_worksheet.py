import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

from sa_package.my_gspread import create_worksheet, update_worksheet_properties, duplicate_worksheet, delete_worksheet, get_worksheet

SCOPE = ["https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"]
CREDS = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/SANDBOX/sandbox_workspace/data_management/dm_workshop/coding_day/key.json", SCOPE)
SH_ID = "1l1LhuVXF5WmRX2V-LnJArAYN3Gc_4mMSWKcCO---Sxg"


## 새로운 워크시트 만들기
create_worksheet(
    sh_id=SH_ID,
    worksheet_name="승아",
    creds=CREDS
)

## 워크시트 속성 변경하기
update_worksheet_properties(
    sh_id=SH_ID,
    worksheet_name="승아",
    properties={
        "index": 1,
        "hidden": True
    },
    creds=CREDS
)

## 기존의 시트 복제하기
duplicate_worksheet(
    sh_id=SH_ID,
    worksheet_name="승아2",
    dup_sheet_id=1719398424,
    # dup_sheet_id=get_worksheet(sh_id=SH_ID, worksheet_name="승아", creds=CREDS).id,
    creds=CREDS
)

## 시트 삭제하기
delete_worksheet(
    sh_id=SH_ID, 
    worksheet_name="승아2",
    creds=CREDS
)