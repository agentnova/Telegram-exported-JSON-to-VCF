import json
import os.path
json_file=input("Enter the json file name :")
if os.path.isfile(f"{json_file}"):
    vcard=""
    read_file=open(json_file, "r",encoding='latin-1').read()
    json_load=json.loads(read_file)
    try:
        for i in range(50000):
            fname = json_load["contacts"]["list"][i]["first_name"]
            lname = json_load["contacts"]["list"][i]["last_name"]
            phone = json_load["contacts"]["list"][i]["phone_number"]
            vcard += f"""BEGIN:VCARD
VERSION:3.0
FN:{fname} {lname}
N:{lname} {fname};;;
TEL;TYPE=CELL:{phone}
END:VCARD
"""
    except IndexError:
        pass
    vcfile="contact.vcf"
    with open(vcfile, "w",encoding='utf-8') as f:
        f.write(vcard)
    print("VCF file has been generated succesfully")
else:
    print("Json file not found")
