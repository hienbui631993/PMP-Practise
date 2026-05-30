import json, re, sys

d = json.load(open("dnd_dataset.json", encoding="utf-8"))
bynum = {}
for q in d:
    if q["number"] <= 89:
        bynum[q["number"]] = q   # dedupe, keep verified Q1-89

missing = [n for n in range(1, 90) if n not in bynum]
if missing:
    open("zout.txt", "w").write("MISSING_LOW=%s count_low=%d" % (missing, len(bynum)))
    sys.exit(50)   # signal: need full rebuild

def it(t, a): return {"text": t, "answer": a}
new = [
 {"number":90,"prompt":"Match each item to the tool it describes.","left_label":"Description","right_label":"Tool",
  "items":[it("Visualizing work in progress.","Kanban Board"),
           it("Allocating fixed periods for activities.","Time-Boxing"),
           it("Visual representation of task relationships.","PDM (Precedence Diagramming Method)")],
  "options":["Kanban Board","Time-Boxing","PDM (Precedence Diagramming Method)"],
  "explanation":"Work-in-progress visualization = Kanban board; fixed time periods = time-boxing; showing task relationships/dependencies = the Precedence Diagramming Method (PDM)."},
 {"number":91,"prompt":"Match each situation to the formula/term.","left_label":"Situation","right_label":"Term",
  "items":[it("Used to estimate task durations using optimistic, pessimistic, and most likely scenarios.","PERT"),
           it("The value of work actually performed, expressed in terms of the budget.","EV (Earned Value)"),
           it("The approved budget assigned to the work scheduled to be completed by a specific time.","PV (Planned Value)"),
           it("A measure of cost efficiency, calculated as the ratio of earned value to actual cost.","CPI (Cost Performance Index)")],
  "options":["EV (Earned Value)","CPI (Cost Performance Index)","PERT","PV (Planned Value)"],
  "explanation":"Three-point (optimistic/pessimistic/most likely) = PERT; work actually performed = EV; budget for scheduled work = PV; EV/AC = CPI."},
 {"number":92,"prompt":"Match each term to its description.","left_label":"Description","right_label":"Term",
  "items":[it("Team norms and behaviors guide project work.","Organizational Culture"),
           it("Central oversight of all project practices.","PMO"),
           it("Systems in place for sharing lessons learned.","Knowledge Management"),
           it("Clearly defined decision-making processes.","Governance Framework")],
  "options":["Knowledge Management","Organizational Culture","PMO","Governance Framework"],
  "explanation":"Norms/behaviors = organizational culture; central oversight = PMO; sharing lessons learned = knowledge management; decision-making processes = governance framework."},
 {"number":93,"prompt":"Match each EVM rule of thumb to the metric it describes.","left_label":"Rule","right_label":"Metric",
  "items":[it("A negative value is bad (behind schedule).","SV (Schedule Variance)"),
           it("A positive value is good (under budget).","CV (Cost Variance)"),
           it("1 or greater is ahead of schedule.","SPI (Schedule Performance Index)"),
           it("Under 1 is over budget.","CPI (Cost Performance Index)")],
  "options":["SPI (Schedule Performance Index)","SV (Schedule Variance)","CV (Cost Variance)","CPI (Cost Performance Index)"],
  "explanation":"Variances: negative SV = behind schedule, positive CV = under budget. Indices: SPI >= 1 = ahead of schedule, CPI < 1 = over budget."},
 {"number":94,"prompt":"Interpret each EVM value.","left_label":"Value","right_label":"Interpretation",
  "items":[it("SV is -200","Over Schedule"),
           it("SPI is 1.4","Ahead Schedule"),
           it("CPI is 1.5","Under Budget"),
           it("CV is -70","Over Budget")],
  "options":["Over Budget","Under Budget","Over Schedule","Ahead Schedule"],
  "explanation":"Negative SV = behind/over schedule; SPI 1.4 (>1) = ahead of schedule; CPI 1.5 (>1) = under budget; negative CV = over budget."},
 {"number":95,"prompt":"Match each description to the organizational structure.","left_label":"Description","right_label":"Structure",
  "items":[it("The project manager has full authority over the project and resources.","Projectized Structure"),
           it("Employees are grouped by specialization and report to a functional manager.","Functional Structure"),
           it("Project managers have limited authority.","Weak Matrix"),
           it("Project managers have considerable authority.","Strong Matrix")],
  "options":["Projectized Structure","Weak Matrix","Functional Structure","Strong Matrix"],
  "explanation":"Full PM authority = projectized; grouped by specialty under functional managers = functional; limited PM authority = weak matrix; considerable PM authority = strong matrix."},
 {"number":96,"prompt":"Match each task to the collaboration tool that best supports it.","left_label":"Task","right_label":"Tool",
  "items":[it("Share and archive project documentation and reference materials.","Online Bulletin Boards"),
           it("Plan and allocate resources, monitor task dependencies, and track project milestones.","Project Management Software"),
           it("Host remote training sessions or workshops for team members and stakeholders.","Video Conferencing")],
  "options":["Video Conferencing","Online Bulletin Boards","Project Management Software"],
  "explanation":"Sharing/archiving docs = bulletin boards; resources/dependencies/milestones = PM software; remote training/workshops = video conferencing."},
 {"number":97,"prompt":"Match each term to its description.","left_label":"Description","right_label":"Term",
  "items":[it("A disruption or delay caused by poor handoff or transition of tasks between team members.","Dropped Baton"),
           it("Individuals add extra time to their task estimates to avoid the risk of missing deadlines.","Self-Protection"),
           it("Procrastination where work is delayed until the last possible moment before the deadline.","Student Syndrome"),
           it("Tasks take longer to complete if more time is allocated to them.","Parkinson's Law")],
  "options":["Student Syndrome","Dropped Baton","Parkinson's Law","Self-Protection"],
  "explanation":"Handover delay = Dropped Baton; padding estimates = Self-Protection; last-minute work = Student Syndrome; work fills the time = Parkinson's Law."},
 {"number":98,"prompt":"Match each description to the schedule tool.","left_label":"Description","right_label":"Tool",
  "items":[it("Visualizing the project schedule and tracking task dependencies.","Gantt Chart"),
           it("Identifying the longest sequence of dependent tasks and optimizing the schedule.","CPM (Critical Path Method)"),
           it("Estimating the amount of time to complete an activity.","PERT")],
  "options":["Gantt Chart","CPM (Critical Path Method)","PERT"],
  "explanation":"Schedule visualization/dependencies = Gantt chart; longest dependent sequence = CPM; activity duration estimate = PERT."},
 {"number":99,"prompt":"Match each description to the schedule tool/technique.","left_label":"Description","right_label":"Tool",
  "items":[it("Tracking key events and progress.","Milestone Chart"),
           it("Finding the longest amount of time to complete a project.","CPM (Critical Path Method)"),
           it("Overlapping activities to shorten duration.","Fast Tracking")],
  "options":["Milestone Chart","CPM (Critical Path Method)","Fast Tracking"],
  "explanation":"Key events/progress = milestone chart; longest path/duration = CPM; overlapping activities to compress = fast tracking."},
 {"number":100,"prompt":"Match each description to the agile/XP technical practice.","left_label":"Description","right_label":"Practice",
  "items":[it("Writing assessments (tests) before developing code to ensure functionality.","TDD (Test-Driven Development)"),
           it("A time-boxed research task to explore or investigate solutions.","Spike"),
           it("Ongoing integration, testing, and delivery of software during development.","Continuous Delivery")],
  "options":["Spike","TDD (Test-Driven Development)","Continuous Delivery"],
  "explanation":"Tests before code = TDD; time-boxed investigation = Spike; ongoing integrate/test/deliver = Continuous Delivery."},
]
out = [bynum[n] for n in range(1, 90)] + new
assert [q["number"] for q in out] == list(range(1, 101))
assert all(all(i["answer"] in q["options"] for i in q["items"]) for q in out)

# recompute video_time
def to_sec(ts):
    p=[int(x) for x in ts.split(":")]; return p[0]*60+p[1] if len(p)==2 else p[0]*3600+p[1]*60+p[2]
toks=[];cur=0
for ln in open("100 pmp dnd.md",encoding="utf-8").read().split("\n"):
    s=ln.strip(); m=re.match(r'^(\d+:\d+(?::\d+)?)$',s)
    if m: cur=to_sec(m.group(1)); continue
    for w in re.sub(r'[^a-z0-9]+',' ',s.lower()).split(): toks.append((cur,w))
ones=["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
def forms(n): return set([str(n)]+([ones[n]] if n<20 else []))
Wd=[w for _,w in toks];Sc=[s for s,_ in toks]
raw=[];start=0
for n in range(1,101):
    f=forms(n);found=None
    for i in range(start,len(Wd)-1):
        if Wd[i] in ("question","number") and Wd[i+1] in f: found=Sc[i];start=i+1;break
    raw.append(found)
known=[(i,v) for i,v in enumerate(raw) if v is not None]
def itp(i):
    if raw[i] is not None: return raw[i]
    pv=[k for k in known if k[0]<i]; nx=[k for k in known if k[0]>i]
    if pv and nx:(a,av),(b,bv)=pv[-1],nx[0];return av+(bv-av)*(i-a)/(b-a)
    if pv:return pv[-1][1]+(i-pv[-1][0])*55
    return nx[0][1]
vals=[int(itp(i)) for i in range(100)]
for i in range(1,100):
    if vals[i]<vals[i-1]: vals[i]=vals[i-1]
for q,v in zip(out,vals): q["video_time"]=v

json.dump(out, open("dnd_dataset.json","w",encoding="utf-8"), indent=2, ensure_ascii=False)
sys.exit(0)
