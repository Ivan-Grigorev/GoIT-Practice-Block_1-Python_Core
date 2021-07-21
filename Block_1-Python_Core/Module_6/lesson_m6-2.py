# import sys
# from pathlib import Path
#
# JPEG_IMAGES = []
# JPG_IMAGES = []
# PNG_IMAGES = []
# SVG_IMAGES = []
# OTHER = []
# ARCH = []
# FOLDERS = []
# UNKNOWN = set()
# EXTENSION = set()
#
# REGISTERED_EXTENSIONS = {
#     "JPEG": JPEG_IMAGES,
#     "JPG": JPG_IMAGES,
#     "PNG": PNG_IMAGES,
#     "SVG": SVG_IMAGES,
#     "ZIP": ARCH
# }
#
#
# def get_extension(file_name) -> str:
#     return Path(file_name).suffix[1:].upper()
#
#
# def scan(folder: Path):
#     for item in folder.iterdir():
#         if item.is_dir():
#             if item.name not in ("JPEG", "JPG", "PNG", "SVG", "OTHER", "ARCH"):
#                 FOLDERS.append(item)
#                 scan(item)
#             continue
#
#         extension = get_extension(item.name)
#         new_name = folder / item.name
#         if not extension:
#             OTHER.append(new_name)
#         else:
#             try:
#                 current_container = REGISTERED_EXTENSIONS[extension]
#                 EXTENSION.add(extension)
#                 current_container.append(new_name)
#             except KeyError:
#                 UNKNOWN.add(extension)
#                 OTHER.append(new_name)
#
#
# if __name__ == "__main__":
#     scan_path = sys.argv[1]
#     print(f"Start in folder {scan_path}")
#
#     search_folder = Path(scan_path)
#     scan(search_folder)
#     print(f"Images jpeg: {JPEG_IMAGES}")
#     print(f"Images jpg: {JPG_IMAGES}")
#     print(f"Images png: {PNG_IMAGES}")
#     print(f"Images svg: {SVG_IMAGES}")
#     print(f"Archives: {ARCH}")
#     print(f"Unknown files: {OTHER}")
#     print(f"There are file of types: {EXTENSION}")
#     print(f"Unknown types of file: {UNKNOWN}")
#
#
# import re
#
# CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
# TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
#                "f", "h", "ts", "ch", "sh", "sch", "", "y", "e", "u", "ja")
#
# TRANS = {}
#
# for cs, trl in zip(CYRILLIC_SYMBOLS, TRANSLATION):
#     TRANS[ord(cs)] = trl
#     TRANS[ord(cs.upper())] = trl.upper()
#
#
# def normalize(name: str) -> str:
#     trl_name = name.translate(TRANS)
#     trl_name = re.sub(r"\W", "_", trl_name)
#     return trl_name
#
#
# import sys
# from pathlib import Path
# import shutil
# import scan
# from normalize import normalize
#
#
# def handle_image(file: Path, root_folder: Path, dist: str):
#     target_folder = root_folder / dist
#     target_folder.mkdir(exist_ok=True)
#     ext = Path(file).suffix
#     new_name = normalize(file.name.replace(ext, "")) + ext
#     file.replace(target_folder / new_name)
#
#
# def handle_other(file, root_folder, dist):
#     target_folder = root_folder / dist
#     target_folder.mkdir(exist_ok=True)
#     ext = Path(file).suffix
#     new_name = normalize(file.name.replace(ext, "")) + ext
#     file.replace(target_folder / new_name)
#
#
# def handle_archive(file: Path, root_folder: Path, dist):
#     target_folder = root_folder / dist
#     target_folder.mkdir(exist_ok=True)  # create folder ARCH
#     ext = Path(file).suffix
#     folder_for_arch = normalize(file.name.replace(ext, ""))
#     archive_folder = target_folder / folder_for_arch
#     archive_folder.mkdir(exist_ok=True)  # create folder ARCH/name_archives
#     try:
#         shutil.unpack_archive(str(file.resolve()), str(archive_folder.resolve()))
#     except shutil.ReadError:
#         archive_folder.rmdir()  # Если не успешно удаляем папку под  архив
#         return
#     file.unlink()  # Если успешно удаляем архив
#
#
# def handle_folder(folder: Path):
#     try:
#         folder.rmdir()
#     except OSError:
#         print(f"Не удалось удалить папку {folder}")
#
#
# def main(folder):
#     scan.scan(folder)
#
#     for file in scan.JPEG_IMAGES:
#         handle_image(file, folder, "JPEG")
#
#     for file in scan.JPG_IMAGES:
#         handle_image(file, folder, "JPG")
#
#     for file in scan.PNG_IMAGES:
#         handle_image(file, folder, "PNG")
#
#     for file in scan.SVG_IMAGES:
#         handle_image(file, folder, "SVG")
#
#     for file in scan.OTHER:
#         handle_other(file, folder, "OTHER")
#
#     for file in scan.ARCH:
#         handle_archive(file, folder, "ARCH")
#
#     for f in scan.FOLDERS:
#         handle_folder(f)
#
#
# if __name__ == "__main__":
#     scan_path = sys.argv[1]
#     print(f"Start in folder {scan_path}")
#
#     sort_folder = Path(scan_path)
#     print(sort_folder)
#     print(sort_folder.resolve())
#     main(sort_folder.resolve())
#
#

# def total_salary(path):
#     total = []
#     fh = open(path, 'r')
#     while True:
#         line = fh.readline()
#         if not line:
#             break
#         line = line.split(",")
#         line1 = line[1]
#         line2 = float(line1)
#         total.append(line2)
#     total1 = sum(total)
#     fh.close()
#     return total1
#
#
#
# def write_employees_to_file(employee_list, path):
#     fh = open(path, 'w')
#     for i in employee_list:
#         for j in i:
#             fh.write("%s\n" % j)
#     symbols = []
#     for line in fh:
#         symbols.append(linе)
#     fh.close()
#     return symbols

#
# def read_employees_from_file(path):
#     list1 = []
#     fh = open(path, 'r')
#     list = fh.readlines()
#     for i in list:
#         i = i.replace("\n", "")
#         list1.append(i)
#     fh.close()
#
#     return list1


# def add_employee_to_file(record, path):
#     fh = open(path, 'a')
#     fh.write(record + "\n")
#     fh.close()
#


#
# def get_cats_info(path):
#     result = []
#     with open(path, "r") as f:
#         for string in f.readlines():
#             id, name, age = string.split(",")
#             result.append({"id": id, "name": name, "age": age.strip()})
#     return result
#
#
#
#
# def get_recipe(path, search_id):
#     with open(path, "r") as f:
#         for line in f.readlines():
#             if search_id in f.readlines():
#                 strings = line.split(",")
#                 result = {"id": search_id, "name": strings[1], "ingredients": strings[2:]}
#                 print(result)
#                 return result
#             else:
#                 return None
#
# def get_recipe(path, search_id):
#     with open(path, 'r') as fh:
#         strings = fh.readlines()
#         result = {}
#         for st in strings:
#             if search_id in st:
#                 id = st.split(",")[0]
#                 name = st.split(",")[1]
#                 ingredients = st.split(",")[2:]
#                 result = {"id": id, "name": name, "ingredients": [i.strip() for i in ingredients[:]]}
#                 return (result)
#
#             elif not str:
#                 break
#
#
# def sanitize_file(source, output):
#     with open(source, 'r') as f:
#         data = ''.join(i for i in f.read() if not i.isdigit())
#     with open(output, 'w') as f1:
#         f1.write(data)
#
#
#

# def save_applicant_data(source, output):
#
#     with open(output, 'w') as f:
#         write_to_file = ''
#         for i in source:
#             data = []
#             for value in i.values():
#                 data.append(str(value))
#             write_to_file += ','.join(data) + '\n'
#         f.write(write_to_file)

# def save_applicant_data(source, output):
#     with open(output, 'w') as fh:
#         st = ""
#         for elem in source:
#             for i, j in elem.items():
#                 st += str(j) + ","
#             st = st[:-1]
#             st += "\n"
#
#         fh.write(st)
#
#
# save_applicant_data([
#     {
#         "name": "Kovalchuk Oleksiy",
#         "specialty": 301,
#         "math": 175,
#         "lang": 180,
#         "eng": 155,
#     },
#     {
#         "name": "Ivanchuk Boryslav",
#         "specialty": 101,
#         "math": 135,
#         "lang": 150,
#         "eng": 165,
#     },
#     {
#         "name": "Karpenko Dmitro",
#         "specialty": 201,
#         "math": 155,
#         "lang": 175,
#         "eng": 185,
#     }
# ])

#
# def is_equal_string(utf8_string, utf16_string):
#     utf8_string1 = utf8_string.decode("utf-8")
#     utf16_string1 = utf16_string.decode("utf-16")
#     if utf8_string1.casefold() == utf16_string1.casefold():
#         return True
#     else:
#         return False
#


# def save_credentials_users(path, users_info):
#     with open(path, 'wb') as f:
#         for key, value in users_info.items():
#             string = ""
#             string += str(key) + ":"
#             string += str(value) + "\n"
#             string = string.encode()
#             f.write(string)
#

#
# def get_credentials_users(path):
#     with open(path, 'rb') as f:
#         new_list = []
#         lines = f.readlines()
#     for line in lines:
#         line = line.decode()
#         new_list.append(line.replace("\n", ""))
#     return new_list
#

#
# import base64
#
#
# def encode_data_to_base64(data):
#     new_list = []
#     for i in data:
#         data_bytes = i.encode("utf-8")
#         base64_bytes = base64.b64encode(data_bytes)
#         base64_data = base64_bytes.decode("utf-8")
#         new_list.append(base64_data)
#     return new_list
#
#
# import shutil
#
#
# def create_backup(path, file_name, employee_residence):
#     with open(path + '/' + file_name, 'wb') as file_name:
#         for key, value in employee_residence.items():
#             string = ""
#             string += str(key) + " "
#             string += str(value) + "\n"
#             string = string.encode()
#             file_name.write(string)
#     archive_name = shutil.make_archive('backup_folder', 'zip', 'folder')
#     return archive_name
#

import shutil


def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path, path_to_unpack)


