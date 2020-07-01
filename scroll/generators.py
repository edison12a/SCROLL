import json

def generate_docs(collected_traces):
    # convert sets to list to avoid JSON serialization error
    for trace_name in collected_traces:
        print(collected_traces[trace_name]['calls'])
        collected_traces[trace_name]['calls'] = list(collected_traces[trace_name]['calls'])

    # write to main file
    with open('traces.json', 'w') as tr:
        tr.write(json.dumps(collected_traces))

    # get the leading/entry function
    numbered_traces = {v['call_number']: v for k, v in collected_traces.items()}
    keys = sorted(list(numbered_traces))
    for num in keys:
        if numbered_traces[num]['calls']:
            entry_function = numbered_traces[num]['function_name']
            break
    # add entry function to traces
    collected_traces['entry_function'] = entry_function
    print('entry_function:', entry_function)

    # create order of functions // classes of docs html file
    order_of_functions = []

    def get_calls(trace_name):
        trace = collected_traces[trace_name]
        for call in trace['calls']:
            order_of_functions.append(collected_traces[call]['function_name'])
            get_calls(collected_traces[call]['function_name'])

    order_of_functions.append(entry_function)
    get_calls(entry_function)

    print(order_of_functions)
