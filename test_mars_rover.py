from mars_rover import MarsRover, Location


class TestMarsRover:

    def test_stays_in_initial_location(self):
        initial_location = Location(x=0, y=0, orientation="N")
        rover = MarsRover(initial_location)
        rover.move("")

        assert rover.location == initial_location
