from oauth2client.service_account import ServiceAccountCredentials

from sa_package.my_gspread import write_values_to_sh

SCOPE = ["https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"]
CREDS = ServiceAccountCredentials.from_json_keyfile_name("./key.json", SCOPE)


write_values_to_sh(
    sh_id="1l1LhuVXF5WmRX2V-LnJArAYN3Gc_4mMSWKcCO---Sxg", #스프레드시트 ID
    worksheet_name="시트1", #워크시트 이름
    start_cell="A1", #값을 입력하기 시작할 셀의 위치
    values=[["테스트1"]], #입력할 값
    creds=CREDS
)

write_values_to_sh(
    sh_id="1l1LhuVXF5WmRX2V-LnJArAYN3Gc_4mMSWKcCO---Sxg",
    worksheet_name="시트1",
    start_cell="A3",
    values=[["1", "2"], ["3", "4"]],
    creds=CREDS
)