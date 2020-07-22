import json
import os
import shutil


def generate_docs(collected_traces, directory='.'):
    package_dir = os.path.dirname(__file__)
    # convert sets to list to avoid JSON serialization error
    for trace_name in collected_traces:
        call_list = list(collected_traces[trace_name]['calls'])
        collected_traces[trace_name]['calls'] = call_list

    # get the leading/entry function
    numbered_traces = {v['call_number']: v for k, v in collected_traces.items()}
    keys = sorted(list(numbered_traces))
    for num in keys:
        if numbered_traces[num]['calls']:
            entry_function = numbered_traces[num]['function_name']
            break
    # add entry function to traces
    collected_traces['entry_function'] = entry_function

     # create order of functions // classes of docs html file
    order_of_functions = []

    def get_calls(trace_name):
        # print(trace_name)
        trace = collected_traces[trace_name]
        # print(trace['calls'])
        for call in trace['calls']:
            order_of_functions.append(collected_traces[call]['function_name'])
            get_calls(collected_traces[call]['function_name'])

    order_of_functions.append(entry_function)
    get_calls(entry_function)


    if not os.path.exists(directory+'/docs'):
        os.makedirs(directory+'/docs')

    # generate documentation in docs folder
    shutil.copy(package_dir+'/templates/index.html', directory+'/docs')
    shutil.copy(package_dir+'/templates/scroll.css', directory+'/docs')

    with open(directory+'/docs/traces_data.js', 'w') as tr:
        tr.write('let traces='+json.dumps(collected_traces))

    with open(directory+'/docs/functions_data.js', 'w') as fc:
        fc.write('let functions='+json.dumps(order_of_functions))
