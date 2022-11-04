from oauth2client.service_account import ServiceAccountCredentials

from sa_package.my_gspread import write_values_to_sh, clear_values

SCOPE = ["https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"]
CREDS = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/SANDBOX/sandbox_workspace/data_management/dm_workshop/coding_day/key.json", SCOPE)
SH_ID = "1l1LhuVXF5WmRX2V-LnJArAYN3Gc_4mMSWKcCO---Sxg"

## 시트에 값 입력하기
write_values_to_sh(
    sh_id=SH_ID, #스프레드시트 ID
    worksheet_name="승아", #워크시트 이름
    start_cell="A1", #값을 입력하기 시작할 셀의 위치
    values=[["테스트1"]], #입력할 값
    creds=CREDS
)

## 시트에 여러 값 입력하기
write_values_to_sh(
    sh_id=SH_ID,
    worksheet_name="승아",
    start_cell="A3",
    values=[["1", "2"], ["3", "4"]],
    creds=CREDS
)

## 시트에서 값 지우기
# clear_values(
#     sh_id=SH_ID,
#     worksheet_name="승아",
#     clear_range="A3:B4",
#     creds=CREDS
# )