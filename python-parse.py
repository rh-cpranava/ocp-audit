import json 
 
log_file_path = r"audit-log-2.log"

def print_full(read_json):
    print(read_json['user']['username'] + ' ' + read_json['annotations']['authorization.k8s.io/decision'] + ' ' + read_json['objectRef']['resource'] + ' ' + read_json['objectRef']['name'] + ' ' + read_json['objectRef']['namespace'])

def print_partial(read_json):
    print(read_json['user']['username'] + ' ' + read_json['annotations']['authorization.k8s.io/decision'])
 
match_list = []
with open(log_file_path, "r") as file:
    list_skip= ["apiserver", "admin", "aggregator"]
    for line in file:
         read_json = json.loads(line)
         try: 
             if any(read_json['user']['username'] in list_element for list_element in list_skip):
                 print_full(read_json)
         except:
             print(read_json)
