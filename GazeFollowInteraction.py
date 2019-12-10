from random import sample


class GazeFollowInteraction:
    RIGHT_HEAD_MOVE = "R"
    LEFT_HEAD_MOVE = "L"

    def __init__(self):
        self.gaze_follow_movements = [GazeFollowInteraction.RIGHT_HEAD_MOVE, GazeFollowInteraction.RIGHT_HEAD_MOVE,
                                      GazeFollowInteraction.RIGHT_HEAD_MOVE, GazeFollowInteraction.LEFT_HEAD_MOVE, GazeFollowInteraction.LEFT_HEAD_MOVE, GazeFollowInteraction.LEFT_HEAD_MOVE]
        self.rand_movements = self._get_random_movements()
        self.curr_mov = 0

    def get_next_move(self):
        
        if self.curr_mov == len(self.rand_movements):
            #print 6/6
            print "6/6 done"
            return  
            # self._reset()
        curr_mov = self.rand_movements[self.curr_mov]
        self.curr_mov += 1
        return curr_mov

    # def _reset(self):
    #     self.rand_movements = self._get_random_movements()
    #     self.curr_mov = 0

    def _get_random_movements(self):
        return sample(self.gaze_follow_movements, len(self.gaze_follow_movements))
