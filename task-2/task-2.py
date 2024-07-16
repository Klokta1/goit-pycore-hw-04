def get_cats_info(path):
    try:
        cats_list = []
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                cat_id, cat_name, cat_age = line.strip().split(',')
                cat_info = {
                    "id": cat_id,
                    "name": cat_name,
                    "age": cat_age
                }
                cats_list.append(cat_info)
        return cats_list
    except FileNotFoundError:
        print("File not found.")
        return []
    except Exception as e:
        print(f"Error during reading file: {e}")
        return []


cats_info = get_cats_info("cats_file.txt")
if cats_info:
    print(cats_info)
else:
    print("Missing cats information.")
