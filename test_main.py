import unittest
from unittest.mock import patch, MagicMock
import turtle
import main

class TestFlappyGame(unittest.TestCase):

    def setUp(self):
        self.player = main.player
        self.pipes = main.pipes
        self.score_writer = main.score_writer

    def test_go_up(self):
        initial_y = self.player.ycor()
        main.go_up()
        self.assertEqual(self.player.ycor(), initial_y + 30)

    def test_gravity(self):
        initial_y = self.player.ycor()
        main.gravity()
        self.assertEqual(self.player.ycor(), initial_y - 2)

    @patch('main.game_over')
    def test_gravity_game_over(self, mock_game_over):
        self.player.sety(-201)
        main.gravity()
        mock_game_over.assert_called_once()

    def test_generate_pipe_top(self):
        pipe = main.generate_pipe_top(100)
        self.assertEqual(pipe.shape(), 'pipetop.gif')
        self.assertEqual(pipe.xcor(), 100)
        self.assertTrue(100 <= pipe.ycor() <= 200)

    def test_generate_pipe_bottom(self):
        pipe = main.generate_pipe_bottom(100)
        self.assertEqual(pipe.shape(), 'pipebottom.gif')
        self.assertEqual(pipe.xcor(), 100)
        self.assertTrue(-200 <= pipe.ycor() <= -100)

    def test_create_pipes(self):
        initial_pipe_count = len(self.pipes)
        main.create_pipes()
        self.assertEqual(len(self.pipes), initial_pipe_count + 2)

    @patch('main.game_over')
    def test_collision_detection(self, mock_game_over):
        pipe = MagicMock()
        pipe.distance.return_value = 50
        self.pipes.append(pipe)
        main.collision_detection()
        mock_game_over.assert_called_once()

    def test_score(self):
        self.player.setx(0)
        pipe = MagicMock()
        pipe.xcor.return_value = 0
        self.pipes.append(pipe)
        initial_score = main.score_var
        main.score()
        self.assertEqual(main.score_var, initial_score + 1)

if __name__ == '__main__':
    unittest.main()