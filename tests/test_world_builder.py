import world_builder


def test_build_world_name():
    expected_name = "Belleville"
    actual_world = world_builder.build_world(name=expected_name)
    assert actual_world["name"] == expected_name
