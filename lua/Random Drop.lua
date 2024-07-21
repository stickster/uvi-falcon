-----------------------------------------------------------------
--! Random Drop
--! Randomly drop events
--! Copyright (C) 2024 Paul W. Frields / Fifth Dominion Studios
--! License: BSD - https://opensource.org/license/bsd-3-clause/
-----------------------------------------------------------------

Label{"Drop events randomly based on probability setting", align = "centred", width = 710}

skipKnob = Knob{"Skip", 0, 0, 1, false, unit = Unit.PercentNormalized}

function onNote(e)
    local myRandom = math.random()
    if (myRandom <= skipKnob.value) then
        return
    else
        playNote(e.note, e.velocity, e.duration, e.layer, e.channel, e.input, e.vol, e.pan, e.tune, e.slice)
    end
end
