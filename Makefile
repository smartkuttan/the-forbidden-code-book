setup:
	python -m venv .venv && . .venv/Scripts/activate && pip install -r env/requirements.txt

test:
	pytest -q

run-ch1:
	python chapters/01-seeds-of-creation/code/spot_forbidden_fruit.py

run-ch2:
	python chapters/02-temptation-of-speed/code/risk_map.py

run-ch3:
	python chapters/03-privacy-in-paradise/code/privacy_minimal.py

run-ch4:
	python chapters/04-whispers-in-the-syntax/code/debug_serpent.py

run-ch6:
	python -m chapters._06_mirror_of_man.code.mirror_test

run-ch7:
	python -m chapters._07_the_fall_into_the_wild.code.watchtower

run-ch8:
	python -m chapters._08_wrath_of_the_world.code.ethical_autopsy

run-ch9:
	python -m chapters._09_guardians_at_the_gates.code.compliance_gate

run-ch10:
	python -m chapters._10_sacred_tools.code.fairness_demo

run-ch11:
	python -m chapters._11_builders_of_the_new_garden.code.new_eden_pipeline

run-ch12:
	python -m chapters._12_prophecies_of_tomorrow.code.prophetic_watchtower




