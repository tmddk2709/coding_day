import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

from sa_package.my_gspread import get_df_from_gspread, write_df_to_sh

SCOPE = ["https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"]
CREDS = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/SANDBOX/sandbox_workspace/data_management/dm_workshop/coding_day/key.json", SCOPE)
SH_ID = "1l1LhuVXF5WmRX2V-LnJArAYN3Gc_4mMSWKcCO---Sxg"

## 데이터 읽어오기
cms_df = get_df_from_gspread(
    sh_id=SH_ID,
    worksheet_name="데이터용",
    read_range="A1:J",
    creds=CREDS
)

print(len(cms_df))

## 데이터 쓰기
write_df_to_sh(
    df=cms_df,
    sh_id=SH_ID,
    worksheet_name="승아",
    include_header=True,
    creds=CREDS
)

## TODO
## 침착맨 데이터만 '침착맨' 시트 만들어서 기록하기
# HINT : chim_df = cms_df.loc[cms_df['크리에이터명'] == '침착맨']
