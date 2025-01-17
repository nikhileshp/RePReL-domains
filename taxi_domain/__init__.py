from gym.envs.registration import register
from taxi_domain.envs.taxiworld_gen import eight_layout, five_by_five_layout


register(
    id='RelationalTaxiWorld-task1-v1',
    entry_point='taxi_domain.envs:RelationalTaxiWorld',
    kwargs={'obs_type': "vec", 'layout': eight_layout,
            'passenger_count': 1, "max_passenger": 3}
)

register(
    id='RelationalTaxiWorld-task2-v1',
    entry_point='taxi_domain.envs:RelationalTaxiWorld',
    kwargs={'obs_type': "vec", 'layout': eight_layout,
            'passenger_count': 2, "max_passenger": 3}
)


register(
    id='RelationalTaxiWorld-task3-v1',
    entry_point='taxi_domain.envs:RelationalTaxiWorld',
    kwargs={'obs_type': "vec", 'layout': eight_layout,
            'passenger_count': 3, "max_passenger": 3}
)




register(
    id='RelationalTaxiWorld-graph-task1-v1',
    entry_point='taxi_domain.envs:RelationalTaxiWorld',
    kwargs={'obs_type': "graph", 'layout': eight_layout,
            'passenger_count': 1, "max_passenger": 3}
)

register(
    id='RelationalTaxiWorld-graph-task2-v1',
    entry_point='taxi_domain.envs:RelationalTaxiWorld',
    kwargs={'obs_type': "graph", 'layout': eight_layout,
            'passenger_count': 2, "max_passenger": 3}
)


register(
    id='RelationalTaxiWorld-graph-task3-v1',
    entry_point='taxi_domain.envs:RelationalTaxiWorld',
    kwargs={'obs_type': "graph", 'layout': eight_layout,
            'passenger_count': 3, "max_passenger": 3}
)

register(
    id='RelationalTaxiWorld-graph-task4-v1',
    entry_point='taxi_domain.envs:RelationalTaxiWorld',
    kwargs={'obs_type': "graph", 'layout': eight_layout,
            'passenger_count': 5, "max_passenger": 5}
)

register(
    id='RelationalTaxiWorld-task1-v2',
    entry_point='taxi_domain.envs:RelationalTaxiWorld',
    kwargs={'obs_type': "vec", 'layout': eight_layout,
            'passenger_count': 1, "max_passenger": 3}
)


register(
    id='RelationalTaxiWorld-task2-v2',
    entry_point='taxi_domain.envs:RelationalTaxiWorld',
    kwargs={'obs_type': "vec", 'layout': eight_layout,
            'passenger_count': 2, "max_passenger": 3}
)


register(
    id='RelationalTaxiWorld-task3-v2',
    entry_point='taxi_domain.envs:RelationalTaxiWorld',
    kwargs={'obs_type': "vec", 'layout': eight_layout,
            'passenger_count': 3, "max_passenger": 3}
)

register(
    id='RelationalTaxiWorld-task1-v3',
    entry_point='taxi_domain.envs:RelationalTaxiWorld',
    kwargs={'obs_type': "vec", 'layout': five_by_five_layout, "max_passenger": 2,
            'passenger_count': 1}
)

register(
    id='RelationalTaxiWorld-task1-v4',
    entry_point='taxi_domain.envs:RelationalTaxiWorld',
    kwargs={'obs_type': "dict", 'layout': five_by_five_layout, "max_passenger": 2,
            'passenger_count': 1}
)


