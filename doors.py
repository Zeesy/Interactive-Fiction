#based on ex31 from Learn Python the Hard Way.
while True:
	print "You enter a dark room with three doors. Do you go through door #1, door #2 or door #3?"

	door = raw_input("> ")

	if door == "1":
		print "There are several coyotes dancing around the body of a deer. Between you and the coyotes is a large tree that has fallen over and begun to rot. What do you do?"
		print "1. Rush up to the coyotes with your arms in the air."
		print "2. Howl."
		print "Hide."

		coyote = raw_input("> ")

		if coyote == "1":
			print "The coyotes rush over and eat your face off. You see nothing but red, turning slowly to black."
			break
		elif coyote == "2":
			print "The coyotes tush over and maul your legs. You feel nothing as they devour you, bleeding to death before they are sated."
			break
		elif coyote == "Hide":
			print "Crouched behind the log you close your eyes and hope they can't hear you breathing or smell your fear. The air around you grows cold, and the sounds of the coyotes celebrating slowly die down into absolute quiet. You raise your head above the log, and see only darkness around you."
			walk = raw_input ("Do you walk into the darkness, or back out the door? \n> ")
			if walk == "darkness":
				print "You keep walking and walking through impenetrable darkness. Eventually you see a faint glow, that eventually resolves itself into several lights. You walk and walk and walk, but never reach them."
				break
			if walk == "door":
				continue
		else:
			print "The coyotes run away as soon as you %s.\n You walk over to the deer's carcas and stick your fingers into the still warm flesh torn open by the coyotes teeth and claws. The deer's eyes turn to you, and it lifts its head slightly. The birds are singing in the trees as you slowly back away, hand covered in blood." % coyote
			break

	elif door == "2":
		print "You are standing at the top of a tall tall tower. You cannot see the ground because there is fog below you, but far in the distance you can see the tops of other towers poking up through the mist."
		print "1. Walk to the edge of the tower."
		print "2. Take the elevator."
		print "3. Go back through the door."

		insanity = raw_input("> ")

		if insanity == "1":
			print "You look out over the edge and see nothing but fog below you. The wind is cool and steady. A gust comes along and lifts you up into the air. You are pushed higher and higher, seeing nothing but fog and the tops of towers endlessly in all directions. The sun grows brighter above you, even as the air gets colder and thinner. Eventually, the curve of the Earth becomes distinct on the horizon. You're lifted through the stratosphere and into Low Earth Orbit. You drifts at the border of space, with the stars all around you and Earth below. After many years, your orbit slows and your body crashes back through the atmosphere and lands in the ocean."
		if insanity == "2":
			print "The elevator is luxurious, with rare woods inlaid in complex patterns, heavy velvets and silvered mirrors. There is the nearly inaudible sound of waves hitting a shoreline, but you cannot see any speakers."
			button = raw_input("What floor do you press?")
			if button == "1" or "ground":
				print "The elevators descent feels rapid, but takes a very long time. Eventually, a soft chime sounds and the doors open on to a wide, sunlit meadow. You step outside into the scent of grass and herbs. As you walk into the meadow the grass grows taller around you until it towers above your head. The grass itself has not grown: rather it is you that has shrunk. Every step you take makes you smaller and smaller until you are walking around pieces of dirt that have become like boulders, and avoiding ants for fear that their feet will crush you. You eventually find yourself floating between particles, so small that you penetrate the cell walls of bacteria, where you are broken apart into your basic elements and redistributed throughout the orgranism."
				break
			if button = "basement"
				print "You enter a large chamber carved from creamy marble shot through with veins of blue-grey. The sounds of several steady drips overlay one another. You think you can hear a pattern, but just as it is about to resolve itself there is a break and you lose it. As you walk out into the room you can see the marble walls reflected in the water that pools in several places on the ground. As you walk forward you begin to notice that your feet are wet. Soon, your legs are wet to the knees, then up to your waist. But you don't care. The water is as warm as your body, and you feel like you could float. You walk until the water is above your head and the sound of the dripping has stopped. But you do not float."
				break
			else:
				print "You hear a soft chime and the doors open."
				continue

		else:
			continue

	elif door == "3":
		foggy = raw_input("The room is filled with fog. Do you want to go in?")
		if foggy == "yes":
			print "The fog feels cool and smells faintly of lavender and oranges. You think you hear the door close softly behind you."
			butterflies = raw_input("Many small, soft lights begin to float gently around the room. You try to catch them, but they are quick to get away. You just want to hold one in your hand. Your attempts to grab one are increasingly chaotic, but you cannot stop. As you leap forward you fall, and there is no floor to stop you. Before you can understand what has happened, you hit the ground and that is all.")
			break
		if foggy = "no":
			continue

	else:
		print "You find yourself growing very, very tired. You're driven to keep moving, but the slightest, most gentle motion requires great effort. You find that it is easiest to lower yourself to the floor, where you lay as you land. Your eyes close, and your breathing becomes slower and slower. You stop moving, stop thinking, and slowly turn to stone."
		break
