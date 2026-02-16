import pytest
import os
import pandas as pd
import hw5pandas as hw5

is_1924 = hw5.athlete_data["Year"] == 1924
dataset_only_1924 = hw5.athlete_data[is_1924]
df = hw5.filter_data(dataset_only_1924)

is_2012 = hw5.athlete_data["Year"] == 2012
is_2014 = hw5.athlete_data["Year"] == 2014
dataset_only_2012_14 = hw5.athlete_data[is_2014 | is_2012]
df2 = hw5.filter_data(dataset_only_2012_14)

def test_filter_data_shape() -> None:
    columns = df.shape[1]
    assert columns <= 10 and columns >= 4


def test_filter_data_shape_2() -> None:
    columns = df2.shape[1]
    assert columns <= 10 and columns >= 4


def test_filter_data_only_winter() -> None:
    df_not_winter = df[df["Season"] != "Winter"]

    rows = df_not_winter.shape[0]
    assert rows == 0


def test_filter_data_only_winter_2() -> None:
    df_not_winter = df2[df2["Season"] != "Winter"]

    rows = df_not_winter.shape[0]
    assert rows == 0


def test_filter_data_only_medals() -> None:
    df_not_medals = df[df["Medal"] == "NA"]

    rows = df_not_medals.shape[0]
    assert rows == 0


def test_filter_data_only_medals_2() -> None:
    df_not_medals = df2[df2["Medal"] == "NA"]

    rows = df_not_medals.shape[0]
    assert rows == 0


def test_filter_data_ids() -> None:
    assert df.duplicated(subset=['ID', 'Year']).sum() == 0


def test_filter_data_ids_2() -> None:
    assert df2.duplicated(subset=['ID', 'Year']).sum() == 0


def test_create_medal_data() -> None:
    index = pd.MultiIndex.from_tuples([
        (1, '2010 Winter'),
        (2, '2010 Winter'),
        (1, '2014 Winter'),
        (3, '2014 Winter'),
        (4, '2018 Winter')
    ], names=['ID', 'Games'])

    data = { # USA has two athletes in 2010, Norway has two in 2014, Germany has one in 2018
    'Team':   ['United States', 'United States', 'Norway', 'Norway', 'Germany'],
    'NOC':    ['USA', 'USA', 'NOR', 'NOR', 'GER'],
    'Year':   [2010, 2010, 2014, 2014, 2018],
    'Season': ['Winter']*5,
    'City':   ['Vancouver', 'Vancouver', 'Sochi', 'Sochi', 'Pyeongchang'],
    'Sport':  ['Curling', 'Ice Hockey', 'Skiing', 'Biathlon', 'Luge'],
    'Event':  ['Curling Men', 'Ice Hockey Men', 'Skiing Men', 'Biathlon Men', 'Luge Singles'],
    'Medal':  ['Gold', 'Silver', 'Bronze', 'Gold', 'Silver']
    }

    df = pd.DataFrame(data, index=index)

    actual = hw5.create_medal_data(df)
    expected = pd.DataFrame(
        {
            "Year": {0: 2010, 1: 2014, 2: 2018},
            "NOC": {
                0: "USA",
                1: "NOR",
                2: "GER",
            },
            "Decorated_Athletes": {0: 2, 1: 2, 2: 1},
        }
    )

    expected2 = pd.DataFrame(
        {
            "Year": {0: 2018, 1: 2014, 2: 2010},
            "NOC": {
                0: "GER",
                1: "NOR",
                2: "USA",
            },
            "Decorated_Athletes": {0: 1, 1: 2, 2: 2},
        }
    )
    cols = ["Year", "NOC", "Decorated_Athletes"]
    try:
        pd.testing.assert_frame_equal(actual[cols], expected[cols])
    except AssertionError:
        pd.testing.assert_frame_equal(actual[cols], expected2[cols])


def test_create_ranking_dict() -> None:
    medal_data = pd.DataFrame(
        {
            "Year": {0: 2010, 1: 2014, 2: 2018},
            "NOC": {
                0: "USA",
                1: "NOR",
                2: "GER",
            },
            "Decorated_Athletes": {0: 2, 1: 2, 2: 1},
        }
    )

    actual = hw5.create_ranking_dict(medal_data)
    expected = {
        2010: [{'NOC': 'USA', 'Decorated_Athletes': 2, 'Flag': 'united-states.bmp'}],
        2014: [{'NOC': 'NOR', 'Decorated_Athletes': 2, 'Flag': 'norway.bmp'}],
        2018: [{'NOC': 'GER', 'Decorated_Athletes': 1, 'Flag': 'germany.bmp'}]
    }

    assert actual == expected