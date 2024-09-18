import json
import xmltodict

filename = "tm.json"

data = open(filename, 'r')
tm = json.load(data)

print(data)

print(tm)
print(tm["q0"])
print(tm["F"])

q = "q2"
print(tm["Delta"][q])
print(q in tm["F"])

# 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 XML EXAMPLE 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
d = xmltodict.parse("""
<structure>
    <type>turing</type>
    <automaton>
        <!--The list of states.-->
        <block id="1" name="q1">
            <tag>Machine1</tag>
            <x>748.0</x>
            <y>212.0</y>
            <final/>
        </block>
        <block id="2" name="q2">
            <tag>Machine2</tag>
            <x>386.0</x>
            <y>210.0</y>
            <initial/>
        </block>
        <!--The list of transitions.-->
        <transition>
            <from>2</from>
            <to>1</to>
            <read/>
            <write/>
            <move>S</move>
        </transition>
        <transition>
            <from>2</from>
            <to>2</to>
            <read>0</read>
            <write>1</write>
            <move>R</move>
        </transition>
        <transition>
            <from>2</from>
            <to>2</to>
            <read>1</read>
            <write>0</write>
            <move>R</move>
        </transition>
        <!--The list of automata-->
        <Machine2/>
        <Machine1/>
    </automaton>
</structure>
        """)
print(json.dumps(d, indent=4))

with open("../tests/p2/0n1m.jff", 'r') as f:
    doc = xmltodict.parse(f.read())
    print(doc)
