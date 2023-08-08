import requests

gov_emissions_factors = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1166236/ghg-conversion-factors-2023-condensed-set-update.xlsx"
gov_emissions_factors_flat = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1105317/ghg-conversion-factors-2022-flat-format.xls"

filepath = "data-raw/gov_emissions.xlsx"
flat_path = "data-raw/gov_emissions_flat_file.xlsx"
# with requests.get(gov_emissions_factors, stream=True) as r:
#     with open(filepath, "wb") as f:
#         for chunk in r.iter_content(chunk_size=16*1024):
#             f.write(chunk)
def download_file(url, filepath):
    response = requests.get(url)
    with open(filepath, "wb") as f:
        f.write(response.content)

if __name__ == "__main__":
    #download_file(gov_emissions_factors, filepath)
    download_file(gov_emissions_factors_flat, flat_path)