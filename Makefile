.PHONY: answers

answer/%: %/answer.py
	python3 $<
