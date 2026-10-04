from .ollama import chat

SUITE={
"general":[("What is the capital of France?","Paris"),("What is 12 multiplied by 8?","96"),("Name one primary color.","red")],
"coding":[("What keyword defines a function in Python?","def"),("What data structure stores key-value pairs in Python?","dictionary"),("What does HTTP stand for?","hypertext transfer protocol")],
"healthcare":[("What organ pumps blood through the body?","heart"),("What vitamin is commonly produced by sunlight exposure?","vitamin d"),("What does BMI stand for?","body mass index")],
"banking":[("What does ATM stand for?","automated teller machine"),("What is interest on a loan?","cost of borrowing"),("What is a bank deposit?","money placed in a bank account")],
"legal":[("What is a contract?","agreement"),("What does evidence mean in a legal case?","information used to establish facts"),("What is a court?","institution that resolves legal disputes")]
}

async def run_suite(model,categories):
    out=[]
    for cat in categories:
        qs=SUITE.get(cat,[])
        correct=0; lat=[]; tps=[]
        for q,expected in qs:
            res=await chat(model,q)
            text=res["answer"].lower()
            # Simple educational benchmark: keyword match, not a legal/medical evaluation.
            if any(k in text for k in expected.split()): correct+=1
            lat.append(res["latency_ms"]); tps.append(res["tokens_per_sec"])
        acc=100*correct/max(1,len(qs))
        latency=sum(lat)/max(1,len(lat)); speed=sum(tps)/max(1,len(tps))
        score=round((acc/10)*0.75 + min(speed/10,10)*0.15 + max(0,10-latency/1000)*0.10,2)
        out.append({"category":cat,"accuracy":acc,"latency_ms":latency,"tokens_per_sec":speed,"score":score})
    return out
