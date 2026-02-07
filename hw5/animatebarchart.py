"""
CMSC 14200, Winter 2026
Homework 5

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

import pygame
import sys
import time
from rich.live import Live

import hw5pandas
from barchart import BarChart
from graphicalbarchart import GraphicalBarChart
from terminalbarchart import TerminalBarChart

SECONDS_PER_CHART = 1.5

WIDTH = 1200
HEIGHT = 600

GUI_AREA_X = 100
GUI_AREA_Y = 100
GUI_AREA_WIDTH = 600
GUI_AREA_HEIGHT = 300

def run_animation(data: dict, chart: BarChart, screen: pygame.Surface, 
    years: list, starting_data: list, year_index: int):
    clock = pygame.time.Clock()
    time_since_change = 0.0
    running = True

    while running:
        dt = clock.tick(60) / 1000 # seconds since last frame
        time_since_change += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                  running = False

        if time_since_change >= SECONDS_PER_CHART:
            time_since_change = 0.0
            year_index += 1

            if year_index < len(years):
                chart.set_target_data(data[years[year_index]])
                print('displaying',years[year_index])
            else:
                running = False # stop when there's no more data
        
        screen.fill((30, 30, 30)) # clear screen
        chart.update() # animation math
        chart.draw() # draw this data's bar chart
        pygame.display.flip() # update entire display
        
    pygame.quit() # we are done


def run_GUI(data: dict, years: list, starting_data: list, year_index: int):
    pygame.init()
    pygame.display.set_caption("GUIAnimatedBarChart")

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    GUI_chart = GraphicalBarChart(
        screen,
        GUI_AREA_X, GUI_AREA_Y, GUI_AREA_WIDTH, GUI_AREA_HEIGHT,
        starting_data
    )

    run_animation(data, GUI_chart, screen, years, starting_data, year_index)



def run_TUI(data: dict, years: list, starting_data: list, year_index: int):
    chart = TerminalBarChart(starting_data,years[0])
  
    seconds_per_year = 1.5
    elapsed = 0.0

    with Live(chart.draw(), refresh_per_second=20) as live:
        start = time.time()

        while year_index < len(years):
            now = time.time()
            dt = now - start
            start = now
            elapsed += dt

            chart.update()
            live.update(chart.draw())

            if elapsed >= seconds_per_year:
                elapsed = 0
                year_index += 1
                if year_index < len(years):
                    year = years[year_index]
                    chart.year = year
                    chart.set_target_data(data[year])
            time.sleep(0.05)


# use pandas helpers to filter and reshape data
filtered_data = hw5pandas.filter_data(hw5pandas.athlete_data)
medal_data = hw5pandas.create_medal_data(filtered_data)
graph_dict = hw5pandas.create_ranking_dict(medal_data)

if __name__ == "__main__":
    years = sorted(graph_dict.keys())
    starting_data = graph_dict[years[0]]
    year_index = 0

    if len(sys.argv) == 1 or sys.argv[1] == 'tui':
        run_TUI(graph_dict, years, starting_data, year_index)
    elif sys.argv[1] == 'gui':
        run_GUI(graph_dict, years, starting_data, year_index)
    else:
        print(f"Usage: python3 {sys.argv[0]} [tui|gui]")
