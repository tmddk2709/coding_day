import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

from sa_package.my_gspread import write_df_to_sh

SCOPE = ["https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"]
CREDS = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/SANDBOX/sandbox_workspace/data_management/dm_workshop/coding_day/key.json", SCOPE)
SH_ID = "1l1LhuVXF5WmRX2V-LnJArAYN3Gc_4mMSWKcCO---Sxg"


## 데이터프레임 만들기
test_df = pd.DataFrame(
    data={
        "col1":[1, 2, 3],
        "col2":[4, 5, 6]
    }
)

## 데이터프레임 시트에 기록하기
write_df_to_sh(
    df=test_df,
    sh_id=SH_ID,
    worksheet_name="승아",
    include_header=False,
    start_cell="A2",
    creds=CREDS
)

write_df_to_sh(
    df=test_df,
    sh_id=SH_ID,
    worksheet_name="승아",
    include_header=True,
    start_cell="D1",
    creds=CREDS
)