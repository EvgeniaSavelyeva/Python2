import yaml

table = '''- !!python/object/apply:collections.OrderedDict
  - - - articul
      - UX31E
    - - name
      - ASUS ZENBOOK
    - - price
      - '44400'
    - - vendor
      - Asus
    - - country
      - China
    - - images
      - http://shopexpress.difocus.ru/alboms/3/3/zenbook.jpg
- !!python/object/apply:collections.OrderedDict
  - - - articul
      - MBA-123
    - - name
      - 13-inch MacBook Air
    - - price
      - '45000'
    - - vendor
      - Apple
    - - country
      - China
    - - images
      - http://shopexpress.difocus.ru/alboms/3/3/apple-air-13.jpg
- !!python/object/apply:collections.OrderedDict
  - - - articul
      - HD-8838
    - - name
      - Philips Saeco HD 8838
    - - price
      - '27462'
    - - vendor
      - Philips
    - - country
      - Russia
    - - images
      - http://shopexpress.difocus.ru/alboms/3/3/saeco-hd-8838.jpg
- !!python/object/apply:collections.OrderedDict
  - - - articul
      - HD-8838
    - - name
      - Delonghi ECAM 23.210
    - - price
      - '27462'
    - - vendor
      - Delonghi
    - - country
      - Italy
    - - images
      - http://shopexpress.difocus.ru/alboms/3/3/delonghi.jpg'''

with open('write.yml', 'w') as file:
    yaml.dump(table, file, Dumper=yaml.Dumper)

with open('write.yml') as file:
   print(yaml.load(file, Loader=yaml.Loader))