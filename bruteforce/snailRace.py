def maurice_wins(m_snails, s_snails):
	Maurice_wins = 0
	if min(m_snails) > max(s_snails):
		Maurice_wins += 1
	if m_snails[1] > s_snails[0]:
		Maurice_wins += 1
	if m_snails[2] > s_snails[1]:
		Maurice_wins += 1
	
	return Maurice_wins >= 2
	
