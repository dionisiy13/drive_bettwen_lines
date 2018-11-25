class ProportionalGain:

    MAX_RIGHT_SERVO = 130
    MAX_LEFT_SERVO = 55
    MIDDLE_POSITION_SERVO = 92

    @staticmethod
    def calculate(coefficient, value,  center,  road_width):

        error = value - center
        kp = road_width / 2

        if kp == 0:
            return False

	print("ERROR IS " + str(road_width))

        difference = ProportionalGain.MAX_RIGHT_SERVO - ProportionalGain.MAX_LEFT_SERVO


        kp = float(difference) / float(kp)
        kp = float(kp)
        output = (float(coefficient) * float(kp)) * float(error)
        output = output + ProportionalGain.MIDDLE_POSITION_SERVO

	print("OUTPUT IS "+str(output))

        if output > ProportionalGain.MAX_RIGHT_SERVO:
            output = ProportionalGain.MAX_RIGHT_SERVO

        if output < ProportionalGain.MAX_LEFT_SERVO:
            output = ProportionalGain.MAX_LEFT_SERVO

        return (ProportionalGain.MAX_RIGHT_SERVO - output) + ProportionalGain.MAX_LEFT_SERVO
