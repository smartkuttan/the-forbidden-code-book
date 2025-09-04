from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class EthicalAutopsy:
    event: str
    stakeholders: List[str]
    technical_cause: str
    ethical_lapse: str
    lessons: List[str] = field(default_factory=list)

    def derive_lessons(self) -> List[str]:
        text = (self.technical_cause + " " + self.ethical_lapse).lower()
        if "opacity" in text or "black box" in text:
            self.lessons.append("Ensure transparency and interpretability in future designs.")
        if "profit" in text or "speed" in text:
            self.lessons.append("Do not prioritize speed/profit over safety and ethics.")
        if "data" in text and "consent" in text:
            self.lessons.append("Collect and process data with explicit, informed consent.")
        if not self.lessons:
            self.lessons.append("Add ethics review and postmortem steps to deployment.")
        return self.lessons

    def report(self) -> Dict[str, object]:
        return {
            "Event": self.event,
            "Stakeholders": list(self.stakeholders),
            "Technical Cause": self.technical_cause,
            "Ethical Lapse": self.ethical_lapse,
            "Lessons": list(self.lessons),
        }


def demo_report() -> Dict[str, object]:
    case = EthicalAutopsy(
        event="Model harmed users due to unmonitored drift",
        stakeholders=["Users", "Company", "Regulator"],
        technical_cause="Black box model with drift; weak monitoring",
        ethical_lapse="Prioritized speed over safety",
    )
    case.derive_lessons()
    return case.report()


if __name__ == "__main__":
    print(demo_report())


