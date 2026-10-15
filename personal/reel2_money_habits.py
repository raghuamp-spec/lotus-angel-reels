import sys; from plib import *
P = dict(bg_top=(255, 246, 232), bg_bot=(250, 222, 190), dots=[(232, 120, 62, 40), (16, 64, 112, 25), (242, 181, 68, 60)],
         hook_text=(16, 64, 112), hook_accent=(192, 32, 40), pill_bg=(232, 120, 62), pill_fg=(255, 255, 255),
         card=(255, 255, 255), icon_bg=(255, 236, 205), card_title=(16, 64, 112), card_body=(80, 70, 64),
         tag_bg=(192, 32, 40), tag_fg=(255, 255, 255), follow_bg=(16, 64, 112), follow_fg=(255, 255, 255))
R = ListReel(P,
    hook=dict(emoji='💸', lines=['Small money', 'habits that', 'add up'], accent_line=2, size=136, sub='30-second money habits'),
    items=[
        dict(emoji='🔍', title='Audit your subscriptions', line='Cancel the ones you forgot you had'),
        dict(emoji='🤖', title='Automate your savings', line='Move a little on payday, before you can spend it'),
        dict(emoji='⏳', title='Try the 24-hour rule', line='Wait a day before any non-essential purchase'),
        dict(emoji='🛟', title='Build an emergency fund', line='Start small. Even a little cushion helps'),
        dict(emoji='📅', title='Do a weekly money check-in', line='10 minutes to see what came in & went out'),
    ],
    question='Which one are you starting this week?', follow_sub='More money habits soon', item_dur=3.3)
if __name__ == '__main__': R.run('reel2_money_habits', sys.argv)
