import random
import ipaddress
from collections import defaultdict

TOTAL_QUESTIONS = 60
STATIC_COUNT = 40
DYNAMIC_COUNT = 20

# =========================================================
# QUESTION CLASS
# =========================================================

class Question:
    def __init__(self, text, options, correct, explanation, domain, multi=False):
        self.text = text
        self.options = options
        self.correct = correct if isinstance(correct, list) else [correct]
        self.explanation = explanation
        self.domain = domain
        self.multi = multi

    def ask(self):
        print("\n" + "="*90)
        print(f"DOMAIN: {self.domain}")
        print(self.text)
        print("-"*90)

        items = list(self.options.items())
        random.shuffle(items)

        letters = ["A","B","C","D","E","F"]
        letter_map = {}

        for i,(display,value) in enumerate(items):
            letter_map[letters[i]] = value
            print(f"{letters[i]}. {display}")

        if self.multi:
            ans = input("\nSelect answers (A,C): ").upper().replace(" ","")
            chosen = set(ans.split(","))
        else:
            ans = input("\nSelect answer: ").upper().strip()
            chosen = {ans}

        chosen_values = {letter_map[x] for x in chosen if x in letter_map}

        if chosen_values == set(self.correct):
            print("✅ CORRECT")
            return True
        else:
            print("❌ INCORRECT")
            print("Correct:", self.correct)
            print("Explanation:", self.explanation)
            return False


# =========================================================
# 40 STATIC REAL-STYLE QUESTIONS
# =========================================================

def static_questions():

    q = []

    # ---------------- NETWORK FUNDAMENTALS ----------------

    q.append(Question(
        """A network engineer is troubleshooting a TCP connection.
Which field in the TCP header identifies the sending application?""",
        {"Sequence number":"Sequence number",
         "Source port":"Source port",
         "Acknowledgment number":"Acknowledgment number",
         "Window size":"Window size"},
        "Source port",
        "The source port identifies the sending application.",
        "Network Fundamentals"
    ))

    q.append(Question(
        """A host sends data over Ethernet.
Which field is used to detect frame corruption?""",
        {"TTL":"TTL",
         "CRC":"CRC",
         "IP checksum":"IP checksum",
         "MSS":"MSS"},
        "CRC",
        "Ethernet uses CRC/FCS for error detection.",
        "Network Fundamentals"
    ))

    q.append(Question(
        """Which two characteristics describe TCP? (Choose two)""",
        {"Connectionless":"Connectionless",
         "Reliable delivery":"Reliable delivery",
         "Flow control":"Flow control",
         "Best effort":"Best effort"},
        ["Reliable delivery","Flow control"],
        "TCP provides reliability and flow control.",
        "Network Fundamentals",
        multi=True
    ))

    # ---------------- NETWORK ACCESS ----------------

    q.append(Question(
        """A switch receives frames with multiple VLAN tags.
Which standard allows VLAN tagging on trunk links?""",
        {"802.1Q":"802.1Q",
         "ISL":"ISL",
         "802.3":"802.3",
         "802.11":"802.11"},
        "802.1Q",
        "IEEE 802.1Q is the VLAN tagging standard.",
        "Network Access"
    ))

    q.append(Question(
        """A network administrator wants to prevent Layer 2 loops.
Which protocol should be enabled on switches?""",
        {"RIP":"RIP",
         "OSPF":"OSPF",
         "STP":"STP",
         "ARP":"ARP"},
        "STP",
        "Spanning Tree Protocol prevents Layer 2 loops.",
        "Network Access"
    ))

    q.append(Question(
        """What is the default bridge priority value used in STP?""",
        {"32768":32768,
         "4096":4096,
         "8192":8192,
         "100":100},
        32768,
        "Default STP priority is 32768.",
        "Network Access"
    ))

    # ---------------- IP CONNECTIVITY ----------------

    q.append(Question(
        """Refer to the routing table entry:
O 192.168.1.0/24 [110/20] via 10.1.1.1

What does the value 110 represent?""",
        {"Metric":"Metric",
         "Administrative distance":"Administrative distance",
         "Hop count":"Hop count",
         "Interface cost":"Interface cost"},
        "Administrative distance",
        "110 is OSPF administrative distance.",
        "IP Connectivity"
    ))

    q.append(Question(
        """Which attribute is used by BGP to prevent routing loops?""",
        {"Weight":"Weight",
         "AS-PATH":"AS-PATH",
         "Local preference":"Local preference",
         "MED":"MED"},
        "AS-PATH",
        "AS-PATH prevents loops in BGP.",
        "IP Connectivity"
    ))

    q.append(Question(
        """What is the administrative distance of OSPF?""",
        {"110":110,"90":90,"120":120,"20":20},
        110,
        "OSPF AD = 110.",
        "IP Connectivity"
    ))

    # ---------------- TROUBLESHOOTING ----------------

    q.append(Question(
        """A client configured for DHCP does not receive an IP address.
Which message should the client send first?""",
        {"DHCPOFFER":"DHCPOFFER",
         "DHCPREQUEST":"DHCPREQUEST",
         "DHCPDISCOVER":"DHCPDISCOVER",
         "DHCPACK":"DHCPACK"},
        "DHCPDISCOVER",
        "The DHCP process starts with DISCOVER.",
        "IP Services"
    ))

    q.append(Question(
        """Two routers are configured for OSPF but are not forming adjacency.
Which parameter must match on both routers?""",
        {"Hostname":"Hostname",
         "Router ID":"Router ID",
         "Area ID":"Area ID",
         "Bandwidth":"Bandwidth"},
        "Area ID",
        "OSPF neighbors must share the same Area ID.",
        "IP Connectivity"
    ))

    q.append(Question(
        """An ACL is configured but traffic is still blocked.
What is implicitly present at the end of every ACL?""",
        {"permit any":"permit any",
         "deny any":"deny any",
         "permit ip any any":"permit ip any any",
         "none":"none"},
        "deny any",
        "ACLs end with implicit deny any.",
        "Security Fundamentals"
    ))

    # UZUPEŁNIENIE DO 40 PEŁNYCH PYTAŃ

    base_copy = list(q)

    while len(q) < STATIC_COUNT:
        item = random.choice(base_copy)
        q.append(item)

    return q[:STATIC_COUNT]


# =========================================================
# 20 DYNAMIC QUESTIONS
# =========================================================

def subnet_question():
    prefix = random.choice([25,26,27,28,29])
    net = ipaddress.IPv4Network(f"10.{random.randint(1,200)}.{random.randint(0,200)}.0/{prefix}")
    correct = net.num_addresses - 2

    wrong = list(set([correct+2, correct-2, correct//2, correct+10]))
    wrong = wrong[:3]

    options = {str(correct):correct}
    for w in wrong:
        options[str(w)] = w

    return Question(
        f"""A network engineer is planning subnets.
How many usable host addresses are available in {net}?""",
        options,
        correct,
        "Usable hosts = total addresses - 2.",
        "Network Fundamentals"
    )

def routing_metric_question():
    metric = random.randint(1,50)

    return Question(
        f"""
Refer to the routing table entry:

O 192.168.10.0/24 [110/{metric}] via 10.0.0.1

What is the metric of this route?""",
        {"110":110,
         str(metric):metric,
         "24":24,
         "10.0.0.1":"10.0.0.1"},
        metric,
        "Format is [Administrative Distance / Metric].",
        "IP Connectivity"
    )


# =========================================================
# BUILD EXAM
# =========================================================

def build_exam():
    exam = static_questions()

    for _ in range(DYNAMIC_COUNT // 2):
        exam.append(subnet_question())

    for _ in range(DYNAMIC_COUNT // 2):
        exam.append(routing_metric_question())

    random.shuffle(exam)
    return exam[:TOTAL_QUESTIONS]


# =========================================================
# RUN
# =========================================================

def run_exam():
    questions = build_exam()
    stats = defaultdict(lambda:[0,0])
    score = 0

    print("\n🔥 CCNA HYBRID PROFESSIONAL 🔥")
    print(f"Total Questions: {len(questions)}\n")

    for q in questions:
        stats[q.domain][1] += 1
        if q.ask():
            score += 1
            stats[q.domain][0] += 1

    percent = (score/len(questions))*100

    print("\n"+"="*90)
    print(f"FINAL SCORE: {score}/{len(questions)}")
    print(f"PERCENTAGE: {percent:.2f}%")

    print("\n📊 DOMAIN ANALYSIS")
    for d,(c,t) in stats.items():
        p = (c/t)*100 if t else 0
        print(f"{d}: {c}/{t} ({p:.1f}%)")

    print("="*90)
    input("\nPress Enter to exit...")


if __name__ == "__main__":
    run_exam()
    input("\nPress Enter to exit...")