import unittest
from unittest.mock import patch, MagicMock
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

    @patch('main.turtle.textinput', return_value='test_user')
    @patch('main.leaderboard.get_leaderboard', return_value=[])
    @patch('main.leaderboard.add_score')
    def test_game_over_new_high_score(self, mock_add_score, mock_get_leaderboard, mock_textinput):
        main.user_name = ""
        main.score_var = 10
        main.game_over()
        mock_textinput.assert_called_once_with("Enter your name", "Enter your name")
        mock_add_score.assert_called_once_with('test_user', 10)
        self.assertTrue(main.game_over_var)

    @patch('main.turtle.textinput', return_value='test_user')
    @patch('main.leaderboard.get_leaderboard', return_value=[{"name": "user1", "score": 5}])
    @patch('main.leaderboard.add_score')
    def test_game_over_existing_high_score(self, mock_add_score, mock_get_leaderboard, mock_textinput):
        main.user_name = ""
        main.score_var = 10
        main.game_over()
        mock_textinput.assert_called_once_with("Enter your name", "Enter your name")
        mock_add_score.assert_called_once_with('test_user', 10)
        self.assertTrue(main.game_over_var)

    @patch('main.turtle.textinput', return_value='test_user')
    @patch('main.leaderboard.get_leaderboard', return_value=[{"name": "user1", "score": 15}])
    @patch('main.leaderboard.add_score')
    def test_game_over_no_high_score(self, mock_add_score, mock_get_leaderboard, mock_textinput):
        main.user_name = ""
        main.score_var = 10
        main.game_over()
        mock_textinput.assert_called_once_with("Enter your name", "Enter your name")
        mock_add_score.assert_not_called()
        self.assertTrue(main.game_over_var)


if __name__ == '__main__':
    unittest.main()