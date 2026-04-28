import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Global Policy Tracker", layout="wide", page_icon="🌍")

st.markdown("""
<style>
    .block-container { padding-top: 1rem; padding-bottom: 1rem; }
    .stat-box { background: white; border-radius: 8px; padding: 0.75rem 1rem;
                border-left: 4px solid #c2185b; margin-bottom: 0.5rem;
                box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
    .stat-num { font-size: 2rem; font-weight: 700; color: #c2185b; line-height: 1; }
    .stat-label { font-size: 0.65rem; color: #999; text-transform: uppercase;
                  letter-spacing: 0.08em; margin-top: 2px; }
</style>
""", unsafe_allow_html=True)

# ── ALL POLICY DATA ───────────────────────────────────────────────────────────
policies = [

    # ── EA (East Asia) ────────────────────────────────────────────────────────
    dict(region="EA (East Asia)", country="South Korea", state="Seoul", city="Seoul",
         lat=37.55, lng=126.99, type="Ordinance", year=2012, status="Passed", scope="City",
         name="Seoul Metropolitan Government Framework Ordinance on Gender Equality",
         what="Foundational legislation for promoting gender equality and expanding participation in society.",
         implementation="Served as basis for policies within the city for eliminating gender discrimination; still in effect.",
         funding="Established Women's Development Fund and mechanisms for accruing finances (Article 31).",
         source="https://legal.seoul.go.kr/legal/english/front%20/page/law.html?pAct=lawView&pPromNo=660"),

    dict(region="EA (East Asia)", country="South Korea", state="Seoul", city="Seoul",
         lat=37.56, lng=127.02, type="Ordinance", year=2011, status="Passed", scope="City",
         name="Seoul Ordinance on the Prevention of Violence Against Women and Protection of Victims",
         what="Standards for prevention of violence against women and protecting victims of GBV.",
         implementation="Part of a long-term initiative (Seoul's Women-Friendly City Project).",
         funding="Mayor may provide financial support; terms are ambiguous.",
         source="https://legal.seoul.go.kr/legal/english/front/page/law.html?pAct=lawView&pPromNo=6412"),

    dict(region="EA (East Asia)", country="South Korea", state="Seoul", city="Seoul",
         lat=37.54, lng=126.97, type="Ordinance", year=2012, status="Passed", scope="City",
         name="Seoul Ordinance on Promotion of Economic Activities of Career-Interrupted Women",
         what="Promotes economic independence for Korean women; encourages re-employment of women whose careers have been interrupted by childcare, pregnancy, or family responsibilities.",
         implementation="Part of a long-term initiative (Seoul's Women-Friendly City Project).",
         funding="No mention of specific funding.",
         source="https://legal.seoul.go.kr/legal/english/front/page/law.html?pAct=lawView&pPromNo=1183"),

    dict(region="EA (East Asia)", country="Japan", state="Osaka", city="Yao",
         lat=34.63, lng=135.60, type="Ordinance", year=2009, status="Passed", scope="City",
         name="Yao City Gender Equality Promotion Ordinance",
         what="Equal participation in policy decision making, increasing compatibility of work and family life, gendered health concerns.",
         implementation="City plan to last from 2021-2025 created in compliance with the ordinance's principles.",
         funding="No mention of funding.",
         source="https://www.city.yao.osaka.jp/_res/projects/default_project/_page_/001/009/626/english0303.pdf"),

    dict(region="EA (East Asia)", country="Japan", state="Tohoku", city="Sendai",
         lat=38.27, lng=140.87, type="Ordinance", year=1966, status="Passed", scope="City",
         name="Sendai City Ordinance for the Promotion of Gender Equality",
         what="Establishes guidelines for promoting gender equality, prioritizing response to the changing socioeconomic landscape.",
         implementation="Information not readily available.",
         funding="Information not readily available.",
         source="https://www.city.sendai.jp/danjo-kikaku/kurashi/manabu/danjo/torikumi/documents/zyourei_3.pdf"),

    dict(region="EA (East Asia)", country="China", state="Shanghai", city="Shanghai",
         lat=31.23, lng=121.47, type="Regulation", year=2022, status="Passed", scope="Municipality-wide",
         name="Regulations of Shanghai Municipality on the Protection of Women's Rights and Interests",
         what="Focuses on anti-harassment, employment equality, voting rights, economic participation, and other ways of uplifting women.",
         implementation="Full implementation seems difficult due to the extensive nature of the regulations.",
         funding="Municipal and district levels must include funds for protection of women's rights in their budgets.",
         source="https://english.shanghai.gov.cn/en-LocalRules/20240920/0c10716cb56344528525de5289a8c9e6.html"),

    dict(region="EA (East Asia)", country="China", state="Guangdong", city="Province-wide",
         lat=23.13, lng=113.27, type="Law", year=2025, status="Passed", scope="Province-wide",
         name="Measures for the Implementation of the Law on the Protection of Women's Rights and Interests in Guangdong Province",
         what="Requires state departments, enterprises, public institutions and mass organizations to promote gender equality in digital fields such as data and personal information processing, automated decision-making and algorithmic recommendation services.",
         implementation="Information not readily available.",
         funding="Information not readily available.",
         source="https://www.chinadaily.com.cn/a/202510/23/WS68f98a7fa310f735438b67ba.html"),

    # ── NA (North America) ────────────────────────────────────────────────────
    dict(region="NA (North America)", country="United States", state="Florida", city="Broward County",
         lat=26.19, lng=-80.37, type="Ordinance", year=2019, status="Passed", scope="City",
         name="Ordinance No. 2019-35 (CEDAW Adoption)",
         what="Adopts CEDAW principles; designates the county auditor to collect gender equity data; amends the code to add powers and responsibilities to the Commission on the Status of Women.",
         implementation="Three biennial reports created on women's economic development, health, safety, and education in Broward County.",
         funding="No information readily available.",
         source="https://library.municode.com/fl/broward_county/ordinances/code_of_ordinances?nodeId=988994"),

    dict(region="NA (North America)", country="United States", state="Montana", city="Bozeman",
         lat=45.68, lng=-111.04, type="Resolution", year=2022, status="Passed", scope="City",
         name="Bozeman City for CEDAW Resolution",
         what="Eliminating all forms of violence against women, girls, trans and non-binary people; promoting health, safety, and equal academic, economic, and business opportunities.",
         implementation="Since 2022: Rally for Reproductive Health and Rights, Women Safety in Public Transportation Campaign, MT Legislative Advocacy on missing and murdered indigenous women.",
         funding="No CEDAW funding yet. Co-leaders hope the City would fund a small grants program.",
         source="https://weblink.bozeman.net/WebLink/DocView.aspx?id=258536&dbid=0&repo=BOZEMAN&cr=1"),

    dict(region="NA (North America)", country="United States", state="California", city="Long Beach",
         lat=33.77, lng=-118.19, type="Resolution", year=2016, status="Passed", scope="City",
         name="CA - Reso. Eliminate Discrimination Against Women, Resolution Number 16-0025",
         what="Supporting CEDAW principles to improve the lives of girls and women in Long Beach; requests a gender analysis study be performed by a City Commission.",
         implementation="Commission on Women and Girls established. No clear evidence the gender analysis study was completed.",
         funding="$25,000 one-time allocation in 2022; $87,000 additional approved for the Commission on Women and Girls.",
         source="https://longbeach.legistar.com/LegislationDetail.aspx?ID=2597404&GUID=17FCAF85-FE48-4E37-B067-EE7391A90CDA"),

    dict(region="NA (North America)", country="Canada", state="Saskatchewan", city="Saskatoon",
         lat=52.16, lng=-106.67, type="Motion", year=2019, status="Passed", scope="City",
         name="National Inquiry into Missing and Murdered Indigenous Women and Girls - Calls for Justice",
         what="Directs city administration to review the Final Report of the National Inquiry into MMIWG and identify how Saskatoon can respond to the Calls for Justice.",
         implementation="Cross-functional team reviewed the report and developed a long-term strategy.",
         funding="Covered by existing budgets; partially funded by First Nations and Metis Community Partnership Projects.",
         source="https://citiesforcedaw.org/wp-content/uploads/2023/09/CEDAW-22_23-Annual-Report-Final.pdf"),

    dict(region="NA (North America)", country="United States", state="Oregon", city="Ashland",
         lat=42.19, lng=-122.70, type="Resolution", year=2016, status="Passed", scope="City",
         name="Ashland CEDAW Resolution",
         what="Supports CEDAW principles; requests a gender analysis study; assuring state funding is designated to address gender-related disparities including domestic violence.",
         implementation="Women's Foundation of Oregon published a report; no clear evidence findings were implemented in Ashland.",
         funding="Assuring state funding designated to address gender-related disparities.",
         source="https://records.ashland.or.us/WebLink/DocView.aspx?dbid=0&id=119845&page=1&cr=1"),

    dict(region="NA (North America)", country="United States", state="South Carolina", city="Columbia",
         lat=34.00, lng=-81.04, type="Resolution", year=2018, status="Passed", scope="City",
         name="Resolution No. R-2018-022",
         what="Declaration supporting elimination of violence against women and equal opportunities. Expresses support for the Cities for CEDAW campaign.",
         implementation="City council shows workshops and help for women in business and empowerment groups.",
         funding="Financial impact section left blank.",
         source="https://citiesforcedaw.org/wp-content/uploads/2020/03/Columbia-CC-CEDAW-Resolution__-March2018-1.pdf"),

    dict(region="NA (North America)", country="United States", state="Wisconsin", city="Madison",
         lat=43.07, lng=-89.40, type="Resolution", year=2019, status="Passed", scope="City",
         name="File 55110: Affirming principles of human rights and equality for women and supporting US ratification of CEDAW",
         what="Affirms support for CEDAW principles; encourages city staff and officials to become familiar with CEDAW; forwards resolution to Congress delegation.",
         implementation="Women's Initiatives Committee later transitioned to voluntary employee-led affinity groups.",
         funding="Nothing mentioned; no specific actions to fund.",
         source="https://citiesforcedaw.org/wp-content/uploads/2020/03/Madison-CEDAW.pdf"),

    dict(region="NA (North America)", country="United States", state="Minnesota", city="Minneapolis",
         lat=44.98, lng=-93.27, type="Resolution", year=2015, status="Passed", scope="City",
         name="Resolution Supporting Cities for CEDAW Initiative",
         what="Eliminate all forms of violence against women and girls, promote their health and safety, and afford them equal academic, economic, and business opportunities.",
         implementation="More a resolution of support. Report on police response to DV calls exists but unclear if related to the CEDAW resolution.",
         funding="Nothing mentioned; no specific actions to fund.",
         source="https://worldwithoutgenocide.org/wp-content/uploads/2021/01/Minneapolis-CEDAW-resolution-12-2015.pdf"),

    dict(region="NA (North America)", country="United States", state="Minnesota", city="Edina",
         lat=44.89, lng=-93.35, type="Resolution", year=2016, status="Passed", scope="City",
         name="Resolution No. 2016-30",
         what="Eliminate all forms of violence against women and girls, promote their health and safety, and afford them equal academic, economic, and business opportunities.",
         implementation="Human Rights and Relations Commission developed a comprehensive plan using the CEDAW resolution as a framework.",
         funding="Nothing mentioned; no specific actions to fund.",
         source="https://worldwithoutgenocide.org/wp-content/uploads/2015/09/Edina-resolution-3-2-2016-signed.pdf"),

    dict(region="NA (North America)", country="United States", state="Utah", city="Salt Lake City",
         lat=40.76, lng=-111.89, type="Ordinance", year=2022, status="Passed", scope="City",
         name="Convention on the Elimination of all Forms of Discrimination Against Women (CEDAW) and Gender Equity Ordinance Number 43",
         what="Analyzes city operations, policies, and programs to advance the elimination of discrimination against women and girls. Establishes the position of Chief Equity Officer, an Intersectional Gender Analysis and Action Plan, and outlines goals around economic development, violence against women, education, and city services.",
         implementation="Establishes the Chief Equity Officer who oversees a citywide equity master plan, language access policy, and provides administrative support to multiple equity commissions. Includes a compensation policy premised on equal pay for equal work.",
         funding="No information readily available except for a budgetary request follow up noted in meeting minutes.",
         source="https://webdme.slcgov.com/AdoptedLegislation/DocView.aspx?id=4693772&dbid=0&repo=SLC&cr=1"),

    dict(region="NA (North America)", country="Canada", state="Ontario", city="Ottawa",
         lat=45.42, lng=-75.70, type="Approved Strategy", year=2021, status="Passed", scope="City",
         name="Women and Gender Equity Strategy (WGES)",
         what="Ensures City services, strategies, and plans integrate a women and gender lens and proactively promote women and gender equity. Works to remove systemic barriers that hinder intersectional groups of women and gender diverse persons.",
         implementation="Implemented by the Gender and Race Equity, Indigenous Relations, Diversity and Inclusion Branch. Involved engagement of 590 staff and residents to collect feedback. Includes staff training, review of data systems through a gender equity lens, and a 2021-2025 implementation plan.",
         funding="No financial implications associated with report recommendations; COVID cited as a potential reason funds might be diverted.",
         source="https://ottawa.ca/en/city-hall/creating-equal-inclusive-and-diverse-city/women-and-gender-equity-strategy/women-and-gender-equity"),

    dict(region="NA (North America)", country="United States", state="Florida", city="Miami-Dade",
         lat=25.55, lng=-80.63, type="Ordinance", year=2015, status="Passed", scope="City",
         name="Ordinance No. 15-87 (CEDAW Ordinance)",
         what="Proactively improves the status of women in the community and advances gender equity policies. Mandates annual analysis comparing growth and advancement of women and girls in health, education, and economic development. Tasks the Office of the Commission Auditor with gathering gender equity data.",
         implementation="The auditor's office has followed through with gathering data and publishing yearly reports. The Commission for Women creates reports with recommendations based on the data. Concrete changes include police recording human trafficking separately from other sex crimes, providing resource sheets to women leaving shelters or jail, and vendor equal pay pledges. However the ordinance did not mandate the County create policies in response to the data.",
         funding="The only budget attached to the ordinance were funds to cover the production of the annual report.",
         source="https://www.miamidade.gov/govaction/legistarfiles/Matters/Y2021/212741.pdf"),

    dict(region="NA (North America)", country="United States", state="New York", city="Westchester County",
         lat=41.0534, lng=-73.7949, type="Resolution", year=2020, status="Passed", scope="County-wide",
         name="CEDAW Resolution (Westchester County)",
         what="Commits Westchester County to eliminating all forms of discrimination and violence against women and girls, promoting their health and safety, and affording them equal academic, economic, social, cultural, political, and business opportunities. Calls on the County Human Rights Commission to implement CEDAW principles.",
         implementation="The County has an Office for Women serving as a central resource on domestic violence, sexual assault, stalking, sexual harassment, legal issues, employment, childcare, education, equal pay, financial planning, and women's health. Also has a Minority and Women Business Enterprises (MWBE) Program. Unclear if these are direct results of the CEDAW resolution.",
         funding="The budget and appropriations committee signed the resolution but no specific funding was mentioned.",
         source="https://drive.google.com/file/d/1vHUYZscZtC3YSAbPm-Acnbp62TJLH8Ah/view"),

    dict(region="NA (North America)", country="United States", state="New York", city="Mount Vernon",
         lat=40.9126, lng=-73.8371, type="Resolution", year=2015, status="Passed", scope="City",
         name="A Resolution Supporting the Cities for CEDAW Campaign (Mount Vernon, NY)",
         what="Commits the city to eliminating all forms of discrimination and violence against women and girls and promoting equal opportunities. Described as the first step in adopting future CEDAW-related ordinances, which could include a task force on the status of women and directing the city human rights commission with local CEDAW implementation.",
         implementation="The future ordinances discussed in the resolution do not appear to have been passed. More a general resolution of support with no concrete actions.",
         funding="Nothing mentioned; no specific actions to fund.",
         source="https://citiesforcedaw.org/wp-content/uploads/2020/03/CEDAW-Resolution-City-of-Mount-Vernon-NY.pdf"),

    dict(region="NA (North America)", country="United States", state="Kentucky", city="Louisville",
         lat=38.2527, lng=-85.7585, type="Resolution", year=2014, status="Passed", scope="City",
         name="A Resolution Supporting Cities for CEDAW Initiative (Louisville)",
         what="Commits Louisville Metro Government to eliminating all forms of violence against women and girls, promoting their health and safety, and affording them equal academic, economic and business opportunities. Described as the first step toward adopting a future ordinance calling for a gender analysis of all departments, an oversight body, and dedicated resources.",
         implementation="The future ordinances discussed do not appear to have been passed. More a general resolution of support with no concrete actions.",
         funding="Nothing mentioned; no specific actions to fund.",
         source="https://citiesforcedaw.org/wp-content/uploads/2020/03/LouisvilleCEDAWFinalVersion082414.pdf"),

    dict(region="NA (North America)", country="United States", state="Pennsylvania", city="Pittsburgh",
         lat=40.4406, lng=-79.9959, type="Ordinance", year=2016, status="Passed", scope="City",
         name="Pittsburgh Gender Equity Commission Ordinance",
         what="Creates a Gender Equity Commission tasked with developing an intersectional gender analysis implementation plan, studying discrimination against all women, giving departments action plans, and ensuring they are implemented. The analyses inform a Five Year Plan and a citywide action plan to integrate human rights principles and implement CEDAW locally.",
         implementation="The Gender Equity Commission website is active and publishing gender analyses reports and policy recommendations. Currently in phase two of the city-wide report. Higher levels of implementation than many other cities.",
         funding="No specific budget mentioned in legislation but the commission is clearly funded and active.",
         source="https://pittsburgh.legistar.com/LegislationDetail.aspx?ID=2866138&GUID=68DCC80C-B0A1-4DB0-A020-03954A6F86B9"),

    dict(region="NA (North America)", country="United States", state="Ohio", city="Granville",
         lat=40.0639, lng=-82.5124, type="Resolution", year=2023, status="Passed", scope="City",
         name="Resolution No. 2023-50 (Granville, Ohio)",
         what="Commits the village to eliminating all forms of discrimination against women and girls, promoting their health and safety, and affording them equal academic, economic and business opportunities.",
         implementation="Nothing much to implement — more a resolution of support. No mention of women or CEDAW in the village's 5-year strategic plan. Initiated by a college student intern who introduced the idea at a council meeting.",
         funding="Nothing mentioned; no specific actions to fund.",
         source="https://static1.squarespace.com/static/5e74de6f4749db7726b1e9fe/t/656e2b1116ae2b0eb5015750/1701718801339/Resolution+No.+2023-50+Supporting+CEDAW.pdf"),

    dict(region="NA (North America)", country="United States", state="Hawaii", city="Honolulu",
         lat=21.3069, lng=-157.8583, type="Ordinance", year=2015, status="Passed", scope="City",
         name="Bill 65 (2015) — Honolulu CEDAW Ordinance",
         what="Adopts and implements the principles of CEDAW at the local level. Requires gender analyses of city department operations, policies, and programs to identify discrimination. Designates the Honolulu County Committee on the Status of Women as the implementing and monitoring agency. Establishes a CEDAW task force and calls for department action plans contributing to a five-year citywide action plan.",
         implementation="The Honolulu County Committee on the Status of Women is active. The specific gender analysis reports and five-year plan are not easily locatable publicly. Similar structure to Pittsburgh's approach.",
         funding="No specific funds or budget mentioned in legislation.",
         source="https://citiesforcedaw.org/wp-content/uploads/2020/03/DOC004-6.pdf"),

    # ── SSEA (South & Southeast Asia) ────────────────────────────────────────
    dict(region="SSEA (South & Southeast Asia)", country="Philippines", state="BARMM", city="Region-wide",
         lat=7.76, lng=124.33, type="Act", year=2018, status="Passed", scope="Region-wide",
         name="Republic Act 11054: Bangsamoro Organic Law (BOL)",
         what="Reserves seats for women in parliament, allocates funding toward gender programs, mandates the inclusion of women in decision-making regarding peace and security.",
         implementation="Information not readily available.",
         funding="Information not readily available.",
         source="https://lawphil.net/statutes/repacts/ra2018/ra_11054_2018.html"),

    dict(region="SSEA (South & Southeast Asia)", country="Philippines", state="Metro Manila", city="Quezon City",
         lat=14.65, lng=121.05, type="Ordinance", year=2014, status="Passed", scope="City",
         name="Ordinance No. SP-2357, S-2014",
         what="Comprehensive anti-discrimination policy on the basis of sexual orientation, gender identity and expression.",
         implementation="Creates programs for reporting cases of discrimination and violence.",
         funding="Allocates 5% of annual budget to finance Gender and Development programs.",
         source="https://pages.upd.edu.ph/sites/default/files/ejmanalastas/files/sp-2357_s-2014-2.pdf"),

    dict(region="SSEA (South & Southeast Asia)", country="India", state="Tamil Nadu", city="State-wide",
         lat=11.13, lng=78.66, type="Amendment", year=2025, status="Passed", scope="State-wide",
         name="Tamil Nadu Prohibition of Harassment of Women (Amendment) Act",
         what="Prevents accused people from being allowed to contact the complainant; expands the existing Tamil Nadu Act 44 of 1998.",
         implementation="Information not readily available.",
         funding="Information not readily available.",
         source="https://prsindia.org/files/bills_acts/bills_states/tamil-nadu/2025/Bill3of2025TN.pdf"),

    dict(region="SSEA (South & Southeast Asia)", country="Pakistan", state="Punjab", city="Province-wide",
         lat=31.17, lng=72.71, type="Act", year=2021, status="Passed", scope="Province-wide",
         name="Punjab Enforcement of Women's Property Rights Act",
         what="Protects and secures the rights of ownership of women in property, ensuring such rights are not violated by means of harassment, coercion, force or fraud.",
         implementation="Information not readily available.",
         funding="Information not readily available.",
         source="https://pcsw.punjab.gov.pk/property_right_act"),

    dict(region="SSEA (South & Southeast Asia)", country="Malaysia", state="Perak", city="Ipoh",
         lat=4.60, lng=101.08, type="Program", year=2022, status="Passed", scope="City",
         name="Basic Sanitary Kit (PROKiS) Programme",
         what="Addresses period poverty by providing sanitary kits with feminine hygiene products and educational pamphlets to young women and girls.",
         implementation="Information not readily available.",
         funding="Information not readily available.",
         source="https://www.perak.gov.my/index.php/en/berita-utama-en/2235-perak-tackles-period-poverty-through-education-infrastructure-and-supply-assistance-26-february-2022"),

    dict(region="SSEA (South & Southeast Asia)", country="Cambodia", state="Kandal", city="Phnom Penh",
         lat=11.56, lng=104.93, type="Sub-Decree", year=2002, status="Passed", scope="National",
         name="Government Rectangular Strategy Phase III",
         what="Mandates that at least one woman hold a leadership position in all levels of government, all the way down to the village level.",
         implementation="Information not readily available.",
         funding="Information not readily available.",
         source="https://www.unwomen.org/sites/default/files/Headquarters/Attachments/Sections/CSW/64/National-reviews/Cambodia.pdf"),

    dict(region="SSEA (South & Southeast Asia)", country="Laos", state="Nationwide", city="Nationwide",
         lat=17.98, lng=102.63, type="Plan", year=2003, status="Passed", scope="Nation-wide",
         name="National Strategy on the Advancement of Women for 2011-2015",
         what="Created Sub-CAW Units to facilitate and monitor CEDAW implementation on all levels of government, including local and village level.",
         implementation="Information not readily available.",
         funding="Information not readily available.",
         source="https://asiapacific.unwomen.org/sites/default/files/Field%20Office%20ESEAsia/Docs/Publications/2011/04-LaoPDR-factsheet.pdf"),

    dict(region="SSEA (South & Southeast Asia)", country="Nepal", state="Bagmati", city="Kirtipur",
         lat=27.67, lng=85.28, type="Framework", year=2021, status="Passed", scope="City",
         name="Gender Equality and Social Inclusion 2077",
         what="Incorporation of GESI priorities into all government actions, such as budgeting, planning, reporting, etc.",
         implementation="Information not readily available.",
         funding="Information not readily available.",
         source="https://www.undp.org/nepal/publications/gender-equality-and-social-inclusion-2077-kirtipur-municipality"),

    dict(region="SSEA (South & Southeast Asia)", country="Pakistan", state="Sindh", city="Province-wide",
         lat=25.89, lng=68.52, type="Act", year=2013, status="Passed", scope="Province-wide",
         name="Domestic Violence (Prevention & Protection) Act",
         what="Increased protection for domestic violence victims, specifically women and children but also mentions other vulnerable individuals more broadly.",
         implementation="Information not readily available.",
         funding="Information not readily available.",
         source="https://sja.gos.pk/assets/Acts_Ordinances_Rules/Domestic%20Violence%20%28Prevention%20and%20Protection%29%20Act%2C%202013%20%26%20Rules%2C%202016%20%28Amendments%20upto%20date%29.pdf"),

    dict(region="SSEA (South & Southeast Asia)", country="Sri Lanka", state="National", city="Nation-wide",
         lat=6.88, lng=79.90, type="Act", year=2016, status="Passed", scope="Nation-wide",
         name="Local Government Authorities (Amendment) Act, No. 1",
         what="Sets standards to ensure political parties nominate woman candidates and that women achieve positions of power through quota systems.",
         implementation="Passed nationally but applies at local government level.",
         funding="Information not readily available.",
         source="https://mpclg.gov.lk/web/images/PDF/laws/Act_No_1E.pdf"),

    dict(region="SSEA (South & Southeast Asia)", country="Bhutan", state="Thimphu District", city="Thimphu",
         lat=27.47, lng=89.64, type="Initiative", year=2022, status="Implemented", scope="City",
         name="Gakey Lamtoen",
         what="Prevention measures for GBV through shifting broader social norms such as gender hierarchy, harsh disciplinary measures toward children, alcohol addiction, and other norms that contribute to domestic violence.",
         implementation="First attempt in 2019-2020 was halted due to COVID-19. Piloted by the Project Steering Committee led by the National Committee for Women and Children.",
         funding="Information not readily available.",
         source="https://www.svri.org/thimphus-new-journey-to-reduce-violence-against-women-and-children-begins-with-innovation/"),

    dict(region="SSEA (South & Southeast Asia)", country="Indonesia", state="Java", city="Surakarta",
         lat=-7.58, lng=110.82, type="Regulation", year=2022, status="Passed", scope="City",
         name="Surakarta Municipality Regulation No. 2 of 2022 on Gender Mainstreaming",
         what="Integrating gender mainstreaming into planning, preparation, implementation, monitoring, and evaluation of regional program policies and development activities.",
         implementation="Mandates gender-conscious review of budgets and existing initiatives.",
         funding="All funding coming from the Local Budget of Central Java Province.",
         source="https://jdih.surakarta.go.id/dokumen-hukum/view-prd/file-name-english?id=4yq87wo6rbj9lnqdmad2kvexp5g43x"),

    dict(region="SSEA (South & Southeast Asia)", country="Indonesia", state="Java", city="Surabaya",
         lat=-7.26, lng=112.75, type="Regulation", year=2019, status="Passed", scope="City",
         name="City Regional Regulation No. 4 of 2019 on Gender Mainstreaming",
         what="Mandating real action in planning, preparation, implementation, budgeting, monitoring and evaluation of gender-responsive program policies and development activities.",
         implementation="Mandates gender-conscious review of budgets and existing initiatives.",
         funding="Information not readily available.",
         source="https://jdih.surabaya.go.id/peraturan/3615"),

    # ── Latin America ─────────────────────────────────────────────────────────
    dict(region="Latin America", country="Argentina", state="Buenos Aires", city="Benito Juárez",
         lat=-37.67, lng=-59.78, type="Ordinance", year=2020, status="Passed", scope="City",
         name="Ordinance No. 5539",
         what="Public officials must be trained to implement CEDAW. The municipality of Benito Juárez mandates training on gender and violence against women for all persons in public service. Establishes who will conduct training, enforcement mechanisms, and annual reporting requirements.",
         implementation="Held a gender perspective training to legislate with equity. The ordinance is posted on the municipality's website.",
         funding="Expenses shall be taken from specific items established annually in the municipal budget.",
         source="https://hcdbenitojuarez.com.ar/legislacion/ordenanza-nro-5539/"),

    dict(region="Latin America", country="Colombia", state="Antioquia", city="Medellín",
         lat=6.23, lng=-75.59, type="Municipal Agreement", year=2007, status="Passed", scope="City",
         name="Acuerdo Municipal 1 de 2007",
         what="Creates the Secretariat for Women, which contributes to equality of rights and opportunities for men and women, reduces discriminatory practices toward women, implements public policy, and ensures budget allocation for gender programs.",
         implementation="The Office of the Secretariat for Women within the mayor's office is still very active today, with public policy and many programs for gender equality.",
         funding="No specific information found; the agreement requires ensuring a budget is allocated.",
         source="https://colectivajusticiamujer.org/product/acuerdo-municipal-nro-1-de-2007-crea-la-secretaria-de-las-mujeres-de-medellin/"),

    dict(region="Latin America", country="Argentina", state="Buenos Aires", city="Buenos Aires",
         lat=-34.60, lng=-58.37, type="Law", year=2000, status="Passed", scope="City",
         name="Ley J - N° 474",
         what="Creates a plan to ensure equality of treatment and opportunity between men and women. Defines gender discrimination, mandates use of a gendered perspective in government policies and evaluations, includes anti-discrimination measures, and requires incorporating women in decision-making.",
         implementation="As of 2025, the Subsecretariat of Civic Culture and Social Responsibility oversees implementation. The Ministry of Economy and Finance directs compliance with the budget rule and publishes an annual report.",
         funding="Updated in 2022 to draw from the General Budget of Expenditures of the Autonomous City of Buenos Aires. A 2019 amendment requires the city budget to use a gender equality perspective.",
         source="https://boletinoficialpdf.buenosaires.gob.ar/util/imagen.php?idn=8264&idf=2"),

    dict(region="Latin America", country="Argentina", state="Córdoba", city="Santa Rosa de Calamuchita",
         lat=-32.07, lng=-64.54, type="Ordinance", year=2020, status="Passed", scope="City",
         name="Ordenanza N° 1794/2020",
         what="Establishes mandatory training on gender and violence against women and non-heteronormative identities for all persons serving in public office at all levels and hierarchies.",
         implementation="Authorizes the Municipal Executive Department to carry out the training. Fully complies with National Law No. 27,499 – Micaela Law on Mandatory Gender Training.",
         funding="Any expenditures needed to comply with the ordinance will fall in the budget for the current year.",
         source="https://www.municipiosantarosa.com.ar/wp-content/uploads/2021/11/ORDENANZA-1794-ADHESION-LEY-MICAELA.pdf"),

    dict(region="Latin America", country="Argentina", state="Chaco", city="Province-wide",
         lat=-26.59, lng=-60.95, type="Law", year=2019, status="Passed", scope="Province-wide",
         name="Adhesión L.N. 27499 - Ley Provincial Natalia Samaniego (Ley Micaela)",
         what="The Province of Chaco adheres to National Law No. 27,499 (Micaela Law), establishing mandatory training on gender issues and violence against women for all individuals working in public service at all levels. Creates a program to promote gender equity through training, workshops, dissemination and prevention campaigns.",
         implementation="The Prosecutor's Office of Administrative Investigations of Chaco held gender trainings and workshops, but no evidence of the required annual report or monitoring website.",
         funding="Expenses will be charged to each jurisdiction according to its nature.",
         source="https://e-legis-ar.msal.gov.ar/htdocs/legisalud/migration/html/33744.html"),

    dict(region="Latin America", country="Argentina", state="Chubut", city="Province-wide",
         lat=-43.68, lng=-69.27, type="Law", year=2020, status="Passed", scope="Province-wide",
         name="Ley VIII N° 12",
         what="The province adheres to the national Micaela Law, establishing mandatory training on gender and violence against women for public workers in the Executive, Legislative, and Judicial branches. Invites municipalities to adhere.",
         implementation="Set up asynchronous self-managed gender training for the legislative branch, police, and health department. Nine different government departments certified courses during 2022.",
         funding="Expenses will be drawn from the budgetary allocations of the relevant public agencies.",
         source="https://legislaturadelchubut.gob.ar/2024/08/09/ley-micaela-definen-el-inicio-de-la-capacitacion-para-todos-los-agentes-de-la-legislatura-del-chubut/"),

    dict(region="Latin America", country="Argentina", state="Salta", city="Province-wide",
         lat=-25.25, lng=-64.72, type="Law", year=2019, status="Passed", scope="Province-wide",
         name="Ley 8139",
         what="Adheres to the national Micaela Law, establishing the Secretariat of Women, Gender and Diversity as the enforcement authority. Implements comprehensive training processes to identify gender inequalities and develop eradication strategies.",
         implementation="Trained 900 officers of the Police of the Province of Salta and agents of the Penitentiary Service. Workplace violence training given in towns across the province. Maintains a public registry of all officials who have completed training.",
         funding="No information found.",
         source="https://mujeresydiversidad.salta.gob.ar/ley-micaela/#"),

    dict(region="Latin America", country="Argentina", state="La Rioja", city="Province-wide",
         lat=-29.90, lng=-66.99, type="Law", year=2019, status="Passed", scope="Province-wide",
         name="Ley 10.174",
         what="Adherence to the national Micaela Law for all who work in the Executive, Legislative and Judicial branches of the province. Establishes the Women's Secretariat as enforcement body and mandates annual surveys of training impact indicators.",
         implementation="The Superior Court of Justice of La Rioja developed a training and awareness plan on gender and violence against women in 2021. A Protocol for Intervention in situations of gender-based violence in La Rioja was created.",
         funding="No information found.",
         source="https://www.justicia.ar/novedades/818/2025/06/la-justicia-avanza-en-trabajos-interinstitucionales-del-nuevo-protocolo-de-victimas-de-violencia-de-genero"),

    dict(region="Latin America", country="Argentina", state="Misiones", city="Province-wide",
         lat=-26.94, lng=-54.43, type="Law", year=2019, status="Passed", scope="Province-wide",
         name="Ley IV-N° 85",
         what="Adheres to the national Micaela Law. Creates the Provincial Program of Permanent Institutional Training in Gender Perspective and Violence against Women. Mandates gender training for government agency workers.",
         implementation="The Ministry of Social Development planned comprehensive training on the Micaela Law for all 77 municipalities in Misiones. Monthly mandatory training for those in the Judicial Branch of Misiones.",
         funding="No information found.",
         source="https://src.misiones.gob.ar/ley-micaela-es-una-capacitacion-obligatoria-en-la-provincia-de-misiones/"),

    dict(region="Latin America", country="Argentina", state="Neuquén", city="Province-wide",
         lat=-38.82, lng=-69.67, type="Law", year=2019, status="Passed", scope="Province-wide",
         name="Ley N° 3201-2019",
         what="Adheres to the national Micaela Law. Mandates training for those in extra-power bodies of the provincial state. Establishes the Women's Secretariat as enforcement body and requires annual compliance reports.",
         implementation="The governor signed a decree to regulate the law and provide mandatory gender training for agents of the three branches in the provincial state.",
         funding="The Executive, Legislative and Judicial Branches are empowered to adapt their budget allocations to comply with this law.",
         source="https://www.contadurianeuquen.gob.ar/wp-content/uploads/2019/11/Ley_3201.pdf"),

    dict(region="Latin America", country="Argentina", state="Santa Cruz", city="Province-wide",
         lat=-48.77, lng=-69.19, type="Law", year=2019, status="Passed", scope="Province-wide",
         name="Ley 3642",
         what="Adheres to the national Micaela Law. Invites municipalities, Honorable Deliberative Councils, and Development Commissions to adhere.",
         implementation="A decree was signed by the governor to regulate the law. Gender issues training is promoted for all areas of the Public Security System. Virtual training sessions have been held.",
         funding="No information readily available.",
         source="https://e-legis-ar.msal.gov.ar/htdocs/legisalud/migration/pdf/33325.pdf"),

    dict(region="Latin America", country="Argentina", state="Córdoba", city="Province-wide",
         lat=-31.42, lng=-64.19, type="Law", year=2019, status="Passed", scope="Province-wide",
         name="Ley 10628",
         what="Adheres to the national Micaela Law. Designates the Ministry of Justice and Human Rights as the enforcement authority. Invites municipalities and communes to adhere.",
         implementation="Established training programs: 6-week modules with minimum score requirements and certificates. Judiciary trainings established.",
         funding="No information readily available.",
         source="https://www.legiscba.gob.ar/micaela/"),

    dict(region="Latin America", country="Brazil", state="Paraná", city="Londrina",
         lat=-23.32, lng=-51.17, type="Law", year=2011, status="Passed", scope="City",
         name="Ordinary Law No. 11368/2011",
         what="Creates the Municipal Plan of Policies for Women (PMPM), which defines guidelines, priorities and actions to be developed by the Executive Branch of Londrina in defense of women's rights. A Monitoring and Evaluation Commission, made up equally of civil society and municipal executive representatives, oversees compliance.",
         implementation="The first PMPM was enacted in 2011. A second edition was developed in 2019 through government and civil society collaboration. A third edition (2023-2026) has since been published.",
         funding="No information readily available.",
         source="https://repositorio.londrina.pr.gov.br/index.php/conselho-direitos-da-mulher/legislacao-21/50293-pmpm-2023-2026-aprovado/file"),

    dict(region="Latin America", country="Brazil", state="Paraná", city="Londrina",
         lat=-23.33, lng=-51.18, type="Law", year=2016, status="Passed", scope="City",
         name="Law No. 12.465",
         what="Creates the Municipal Fund for Women's Rights (FMDM), which encourages raising and applying resources to financially support programs and actions for women's rights in Londrina. Funds support programs by the Municipal Secretariat for Women's Policies and the Municipal Council for Women's Rights.",
         implementation="The Municipal Secretariat of Policies for Women lists managing and administering the Municipal Fund as an active responsibility on the government website.",
         funding="Revenue comes from agreements and contracts of national or international origin, donations, subsidies, funds from the Annual Budget Law, and transfers from federal, state, or other organizations.",
         source="https://www.jusbrasil.com.br/legislacao/4873766352/lei-ordinaria-12465-16-pr-londrina"),

    dict(region="Latin America", country="Brazil", state="Paraná", city="Londrina",
         lat=-23.31, lng=-51.16, type="Resolution", year=2023, status="Passed", scope="City",
         name="Resolution 143",
         what="Creates the Special Prosecutor's Office for Women (PEM) within the Municipality of Londrina. The office promotes women's political participation, handles complaints of gender-based violence and discrimination, monitors gender equality policies, and raises awareness against harassment.",
         implementation="A functioning website for the Special Prosecutor for Women provides resources and allows appointments to be scheduled with the prosecutor.",
         funding="No information readily available.",
         source="https://www.cml.pr.gov.br/proposicoes/pesquisa/0/1/0/40906"),

    dict(region="Latin America", country="Brazil", state="Paraná", city="Londrina",
         lat=-23.34, lng=-51.19, type="Law", year=2023, status="Passed", scope="City",
         name="Law 13,705 — Women's Partners Social Responsibility Seal",
         what="Authorizes the Municipal Executive to create the Social Responsibility Seal 'Women's Partners', granting certification to companies that encourage the hiring of women victims of domestic violence.",
         implementation="The law outlines the procedure for granting and monitoring the seal, but no evidence found of the seal being given out to any companies yet.",
         funding="No information readily available.",
         source="https://www.cml.pr.gov.br/proposicoes/Leis/0/16/0/41033"),

    dict(region="Latin America", country="Brazil", state="Paraná", city="Londrina",
         lat=-23.35, lng=-51.20, type="Law", year=2022, status="Passed", scope="City",
         name="Law 13.477 — Women's Support Program",
         what="Establishes the Women's Support Program, aimed at supporting women in situations of domestic and family violence and in situations of socioeconomic vulnerability. Supports financial autonomy through professional training, government employee training, and informing women of their rights.",
         implementation="The law outlines support for financial autonomy of women in vulnerable situations. No site found indicating work being implemented by this specific program, however other laws directly give women who were victims of domestic violence financial support.",
         funding="No information readily available.",
         source="https://portal.londrina.pr.gov.br/menu-oculto-mulher/legislacao-mulher?start=2"),

    dict(region="Latin America", country="Brazil", state="Paraná", city="State-wide",
         lat=-25.25, lng=-52.02, type="Law", year=2025, status="Passed", scope="State-wide (piloted in 16 municipalities)",
         pilot_municipalities="Apucarana, Araucária, Campo Mourão, Cianorte, Foz do Iguaçu, Francisco Beltrão, Guarapuava, Irati, Loanda, Londrina, Maringá, Pinhais, Ponta Grossa, Quatro Barras, São Miguel do Iguaçu, and Umuarama",
         name="Law 22.323 — Recomeço Program",
         what="Establishes the Recomeço Program and Social Assistance for Women in Paraná. Promotes the autonomy and protection of women in situations of domestic and family violence, including support to move away from aggressors, emergency care, employment aid, and emotional support. Provides a monthly benefit of R$810.50 (with 5% increase for women with children in early childhood, pregnant or breastfeeding women, or those with dependents with disabilities) for 12 months.",
         implementation="Aid has so far been provided to 73 women. Currently in pilot phase across 16 municipalities that have Reference Centers for Assistance to Women in Situations of Violence (CRAM), with gradual expansion planned to other cities in the state.",
         funding="The Secretary of State for Women, Racial Equality and the Elderly coordinates and manages the program. Expenses conditioned to budgetary and financial availability in annual budget laws.",
         source="https://leisestaduais.com.br/pr/lei-ordinaria-n-22323-2025-parana-institui-o-programa-recomeco-e-o-auxilio-social-mulher-paranaense"),

    # ── Oceania ───────────────────────────────────────────────────────────────
    dict(region="Oceania", country="Australia", state="Australian Capital Territory", city="Territory-wide",
         lat=-35.47, lng=149.01, type="Resolution", year=2016, status="Passed", scope="Territory-wide",
         name="ACT Women's Plan 2016-2026",
         what="Gender equality plan for ACT women covering safety, economic security, and health.",
         implementation="Three-year targeted action plans focused on improving safety, economic security, and health of women in Canberra. Includes targeted programs, evaluation, gender analysis across government, and focus on intersectional groups.",
         funding="ACT Government.",
         source="https://www.act.gov.au/__data/assets/pdf_file/0004/2380927/ACT-Womens-Plan-2012-2026.pdf"),

    dict(region="Oceania", country="Australia", state="Victoria", city="Melbourne",
         lat=-37.81, lng=144.96, type="Resolution", year=2020, status="Passed", scope="City",
         name="Creating Communities of Equality and Respect: Women's Safety and Empowerment Action Plan",
         what="Addresses and acts on gendered drivers of violence against women.",
         implementation="Embedding gender equity into council policies, upgrading public spaces, partnering with businesses to address toxic gender norms, initiatives like 'Women Who Walk', mandated gender impact assessments for programs, and piloting free period care products in public facilities.",
         funding="City of Melbourne and Victorian Government initiatives.",
         source="https://www.melbourne.vic.gov.au/creating-communities-equality-and-respect-womens-safety-and-empowerment-action-plan"),

    dict(region="Oceania", country="Australia", state="Victoria", city="City of Greater Dandenong",
         lat=-38.01, lng=145.20, type="Ordinance", year=2015, status="Passed", scope="City",
         name="Diversity, Access and Equity Policy",
         what="Supports the Gender Equality Act 2020. Promotes diversity, access, and equity across the Greater Dandenong community.",
         implementation="Community engagement, allocating 30% of sports field usage to new female and gender diverse teams, and providing funding grants. Last reviewed 2021.",
         funding="The Greater Dandenong Council.",
         source="https://www.greaterdandenong.vic.gov.au/diversity-access-and-equity-policy"),

    dict(region="Oceania", country="Papua New Guinea", state="West New Britain", city="Province-wide",
         lat=-5.70, lng=150.03, type="Resolution", year=2021, status="Passed", scope="Province-wide",
         name="Gender-Based Violence Strategic Plan 2021-2025",
         what="Aims to reduce GBV rates by 50% by 2025.",
         implementation="Money allocated towards enabling infrastructure, building family support centers, and research and development.",
         funding="West New Britain Provincial Administration.",
         source="https://ngbvs.com/west-new-britain-province/"),

    dict(region="Oceania", country="Papua New Guinea", state="Milne Bay", city="Province-wide",
         lat=-10.33, lng=150.18, type="Resolution", year=2021, status="Passed", scope="Province-wide",
         name="Milne Bay Provincial Gender Based Violence Strategy 2021-2025",
         what="Reduce GBV and promote gender equality in Milne Bay.",
         implementation="Establishing Provincial GBV Secretariats, training local responders, and establishing the Milne Bay Provincial Child and Family Services Council.",
         funding="Milne Bay Province.",
         source="https://ngbvs.com/milne-bay-province/"),

    dict(region="Oceania", country="Papua New Guinea", state="East New Britain", city="Province-wide",
         lat=-4.61, lng=151.89, type="Resolution", year=2016, status="Passed", scope="Province-wide",
         name="East New Britain Gender Based Violence Strategic Plan 2016-2020",
         what="Decrease GBV through prevention, empowerment, and other means; aiming for a peaceful society free of violence in East New Britain.",
         implementation="Enhanced GBV support structures including medical services and better advocacy. Established GBV Secretariat.",
         funding="Provincial Government (55,000 kina), Division of Community Development, UNDP/National FSVAC, and donations.",
         source="https://ngbvs.com/east-new-britain-province/"),

    dict(region="Oceania", country="New Zealand", state="Greater Wellington", city="Wellington",
         lat=-41.29, lng=174.78, type="Act", year=2025, status="Passed", scope="Nation-wide",
         name="Crimes Legislation (Stalking and Harassment) Amendment Act 2025",
         what="Increased protections against stalking and harassment.",
         implementation="Passed but not yet in force.",
         funding="Information not readily available.",
         source="https://legislation.govt.nz/act/public/2025/72/en/2025-11-26/#LMS1015346"),

    # ── Western Europe ────────────────────────────────────────────────────────
    dict(region="Western Europe", country="France", state="Loire-Atlantique", city="Nantes",
         lat=47.22, lng=-1.55, type="Initiative", year=2023, status="Passed", scope="City",
         name="City of Nantes for Equality",
         what="Aims to become the first non-sexist city by 2030 by mitigating gender-based violence. Created Citad'Elles, a call center to assist victims of GBV. Uses a gender-sensitive budget.",
         implementation="Redesigning public spaces for women (schoolyards to promote co-education), Citad'elles shelter, renaming streets after women, and improved street lighting.",
         funding="City of Nantes and Nantes Metropolis.",
         source="https://eurocities.eu/latest/how-european-cities-are-championing-gender-equality/"),

    dict(region="Western Europe", country="Belgium", state="Brussels-Capital", city="Brussels",
         lat=50.85, lng=4.35, type="UN Initiative", year=2015, status="Passed", scope="City",
         name="UN Women Safe City and Safe Public Spaces",
         what="Aims to prevent and respond to sexual harassment and sexual violence against women and girls in public spaces.",
         implementation="Undercover police officers to identify intimidation, training module for regional public urban planning services on cybersexism and sexual harassment, training managers on workplace violence impact, and feminizing the names of roads and public spaces.",
         funding="City of Brussels and UN Women.",
         source="https://www.unwomen.org/en/news/stories/2015/11/brussels-goes-orange"),

    dict(region="Western Europe", country="Belgium", state="Brussels-Capital", city="Brussels",
         lat=50.86, lng=4.36, type="Action Plan", year=2023, status="Passed", scope="City",
         name="Nothing Without My Consent Action Plan",
         what="77 measures including safe zones, staff training, enhanced street lighting, and taxi safety codes. Prevention-awareness component informs the public and professionals of existing mechanisms. Action component focuses on training on the 5 Ds (distract, delegate, document, delay and direct).",
         implementation="Funded a full-time coordinator at the nightlife federation to develop training for nightlife venues. Sanctions (fines) not dependent on the judicial system. Prevention awareness campaign in cafes and nightlife. Safe Taxi Code established.",
         funding="City of Brussels.",
         source="https://www.brussels.be/sites/default/files/bxl/RIEN_SANS_MON_CONSENTEMENT.pdf"),

    dict(region="Western Europe", country="Belgium", state="Brussels-Capital", city="Brussels",
         lat=50.84, lng=4.34, type="Action Plan", year=2020, status="Passed", scope="City",
         name="Action Plan for Women-Men Equality",
         what="Integrates gender into the city's policies, combats GBV, promotes equality in the workplace, and raises public awareness and citizen participation.",
         implementation="Appointment of a confidential counsellor for complaints of sexual harassment, detection and adaptation of discriminatory practices, review of promotion systems, and balanced composition of juries.",
         funding="Brussels-Capital Regional Government.",
         source="https://www.brussels.be/action-plan-equality-between-women-and-men"),

    dict(region="Western Europe", country="Belgium", state="Brussels-Capital", city="Brussels",
         lat=50.83, lng=4.33, type="Plan", year=2020, status="Passed", scope="City",
         name="Brussels Plan to Combat Violence against Women",
         what="Focused on Prevention, Protection, Prosecution, and implementing integrated policies against violence against women.",
         implementation="Strengthening 24-hour reception at police stations for GBV, mobile stalking alarms introduced, and mandatory training for civil society workers.",
         funding="Brussels-Capital Regional Government.",
         source="https://equal.brussels/wp-content/uploads/2021/03/Brussels-plan-violence-against-women.pdf"),

    dict(region="Western Europe", country="Spain", state="Biscay", city="Bilbao",
         lat=43.26, lng=-2.93, type="Ordinance", year=2005, status="Passed", scope="City",
         name="Ordinance for the Equality of Women and Men",
         what="Equality plans to eliminate gender-based wage discrimination, mandatory gender impact assessments, increasing safety of accessible public spaces, promotion of inclusive language in public areas, and zero tolerance for GBV. Modified in 2022.",
         implementation="Municipal Equality Units established. Inter-Area Commission created to coordinate equality policies. Workplace Equality Commission created.",
         funding="Bilbao City Council.",
         source="https://www.emakunde.euskadi.eus/contenidos/informacion/english_about_us/eu_def/adjuntos/equality_policies_for_women_and_men_bac.pdf"),

    dict(region="Western Europe", country="France", state="Alpes-Maritimes", city="Nice",
         lat=43.70, lng=7.27, type="Initiative", year=2018, status="Passed", scope="City",
         name="Ask for Angela Initiative",
         what="Code name to protect women experiencing street harassment and improve safety in the nightlife scene.",
         implementation="Established in 83 locations in Nice to protect victims of street harassment. Training for employees in participating businesses. Signage to signal participation in the initiative.",
         funding="Local municipalities.",
         source="https://www.nice-premium.com/assessment-of-the-ask-for-angela-initiative/"),

    dict(region="Western Europe", country="Spain", state="Catalonia", city="Barcelona",
         lat=41.39, lng=2.17, type="Municipal Plan", year=2016, status="Passed", scope="City",
         name="Strategy Against Feminisation of Poverty and Deprivation 2016-2024",
         what="Long-term municipal plan aimed at combating the structural factors that make women more vulnerable to poverty and precariousness.",
         implementation="135 actions including promoting awareness of uses of time, facilitating work-life balance, reducing burden of unpaid work, and supporting care. 72 initiatives, 90% carried out or in progress. 138,600 beneficiaries, 455 enterprises and organizations. 325 programs and 100 campaigns launched. 19 studies conducted. 24,000 women have taken part in 25 programs.",
         funding="Barcelona City Council.",
         source="https://ajuntament.barcelona.cat/usosdeltemps/en/actuacio/strategy-against-feminization-poverty-and-precariousness-barcelona"),

    dict(region="Western Europe", country="Austria", state="Bundesländer", city="Vienna",
         lat=48.21, lng=16.37, type="Initiative", year=1997, status="Passed", scope="City",
         name="Women's Work City",
         what="Gender-sensitive urban planning specifically focused on catering to women's housing, community, and working needs like childcare and safe transit.",
         implementation="Women's Workshop City I at Donaufelder Straße 95-97. A 1998 survey revealed high levels of satisfaction. Frauen-Werk-Stadt II housing project at Troststraße 73-75, which also includes assisted living for seniors.",
         funding="City of Vienna.",
         source="https://lgiu.org/planning-for-inclusivity-how-vienna-built-a-gender-equal-city/"),

    dict(region="Western Europe", country="Austria", state="Bundesländer", city="Vienna",
         lat=48.22, lng=16.38, type="Initiative", year=1991, status="Passed", scope="City",
         name="Women Build the City",
         what="Gender mainstreaming in urban planning in the new Seestadt district.",
         implementation="Naming streets after women, exhibition highlighting women architects, using women architects and planners to complete the district, and wider sidewalks for strollers.",
         funding="City of Vienna.",
         source="https://www.france24.com/en/live-news/20210619-women-build-the-city-vienna-s-space-for-female-architects"),

    # ── Eastern Europe ────────────────────────────────────────────────────────
    dict(region="Eastern Europe", country="Bosnia and Herzegovina", state="Republika Srpska", city="East Ilidža",
         lat=44.25, lng=18.68, type="LAP (Local Action Plan)", year=2016, status="Passed", scope="City",
         name="LAP — Local Action Plan (East Ilidža)",
         what="Focuses on economic empowerment of women, specifically victims of violence.",
         implementation="Funded the space and market stalls for handmade food and souvenirs produced by local women. Created safe conditions for women's economic participation.",
         funding="Information not readily available.",
         source="https://www.inclusivesecurity.org/wp-content/uploads/2016/09/Localization-of-Women-Peace-and-Security-Agenda.pdf"),

    dict(region="Eastern Europe", country="Bosnia and Herzegovina", state="Republika Srpska", city="Vlasenica",
         lat=44.18, lng=18.94, type="LAP (Local Action Plan)", year=2016, status="Passed", scope="City",
         name="LAP — Local Action Plan (Vlasenica)",
         what="Workshop focused on steps to address violations of Law on Protection from Domestic Violence.",
         implementation="Developed a brochure with photos and illustrations demonstrating how to report violence.",
         funding="Information not readily available.",
         source="https://www.inclusivesecurity.org/wp-content/uploads/2016/09/Localization-of-Women-Peace-and-Security-Agenda.pdf"),

    dict(region="Eastern Europe", country="Ukraine", state="Chernihiv", city="Region-wide",
         lat=51.50, lng=31.29, type="RAP (Regional Action Plan)", year=2020, status="Passed", scope="Region-wide",
         name="RAP — Regional Action Plan (Chernihiv)",
         what="Addresses gender equality, women's participation, protection from violence, and gender-sensitive recovery in the context of war and post-war reconstruction. Includes gender-aware disaster and conflict preparedness, support for women with social, medical, legal, and psychological services, and improved governance and monitoring of the WPS agenda.",
         implementation="Involved 20 organizations and institutions. Formal monitoring process conducted and presented publicly. Strong civil society participation through projects, training, and capacity building.",
         funding="Regional and local budgets, State Funds, and international organizations.",
         source="https://1325ukraine.org.ua/en/regional-action-plans-2/"),

    dict(region="Eastern Europe", country="Ukraine", state="Donetsk", city="Region-wide",
         lat=48.02, lng=37.80, type="RAP (Regional Action Plan)", year=2021, status="Passed", scope="Region-wide",
         name="RAP — Regional Action Plan (Donetsk)",
         what="Regional implementation of the Women, Peace and Security (WPS) agenda.",
         implementation="1325 Donetsk Region Coalition of 54 civil society organizations, Donetsk Regional State Administration, administrations of 10 local communities, the Eastern Regional Directorate of the State Border Guard Service, and the State Emergency Service. Coalition actively working on reintegration of female veterans, support to survivors, economic capacity of internally displaced persons, and advocacy for rights of women released from captivity.",
         funding="Ukrainian Women's Fund, UN Women in Ukraine, Donetsk Regional State Administration.",
         source="https://1325ukraine.org.ua/en/regional-action-plans-2/"),

    dict(region="Eastern Europe", country="Ukraine", state="Cherkasy", city="Region-wide",
         lat=49.44, lng=32.06, type="RAP (Regional Action Plan)", year=2021, status="Passed", scope="Region-wide",
         name="RAP — Regional Action Plan (Cherkasy)",
         what="New version of the regional action plan. Includes guidelines on women's and men's needs in peace negotiations and post-conflict recovery, gender-balanced staffing, improved early warning systems with gender-sensitive indicators, and improved legislation and coordination for responding to GBV and sexual harassment.",
         implementation="Capacity building through required trainings, regional monitoring system, assigned deadlines between 2023-2025, built shelters, and expanded support services.",
         funding="State-funded.",
         source="https://1325ukraine.org.ua/en/regional-action-plans-2/"),

    dict(region="Eastern Europe", country="Ukraine", state="Kharkiv", city="Region-wide",
         lat=50.00, lng=36.31, type="RAP (Regional Action Plan)", year=2021, status="Passed", scope="Region-wide",
         name="RAP — Regional Action Plan (Kharkiv)",
         what="Regional implementation of the Women, Peace and Security (WPS) agenda, with a big focus on women in the defense and security sector and higher education.",
         implementation="Research on needs of women working in security and defense sector, information campaigns on admission to higher education in the security and defense sector, gender audit, assessment of needs for women to participate in decision-making, development of thematic courses, training government and civil servants on WPS, and gender analysis of budgets.",
         funding="Ukrainian Women's Fund, Government of Netherlands, Center for Equality Advancement, U.S. Department of State.",
         source="https://1325ukraine.org.ua/en/regional-action-plans-2/"),

    dict(region="Eastern Europe", country="Ukraine", state="Dnipropetrovsk", city="Region-wide",
         lat=48.46, lng=35.05, type="LAP (Local Action Plan)", year=2021, status="Passed", scope="Region-wide",
         name="LAP — Local Action Plan (Dnipropetrovsk)",
         what="Regional implementation of the Women, Peace and Security (WPS) agenda.",
         implementation="Strengthening women's leadership in community decision-making and response mechanisms for GBV and conflict-related sexual violence.",
         funding="Information not readily available.",
         source="https://1325ukraine.org.ua/en/regional-action-plans-2/"),

    dict(region="Eastern Europe", country="Poland", state="Małopolskie", city="Kraków",
         lat=50.06, lng=19.95, type="Initiative", year=2026, status="Passed", scope="City",
         name="Krakowianki Program",
         what="Supports women in the labor market.",
         implementation="Krakowianki Month, 'Entrepreneurial Krakowianki' program, and 'Women on the Run' initiative. Partnered with PTTK Centre for Mountain Tourism and ASPIRE Poland.",
         funding="Municipality of Kraków.",
         source="https://www.krakow.pl"),

    # ── Sub-Saharan Africa ────────────────────────────────────────────────────
    dict(region="Sub-Saharan Africa", country="Nigeria", state="Bauchi State", city="Bauchi",
         lat=10.78, lng=9.99, type="Ordinance", year=2020, status="Passed", scope="State-wide",
         name="Bauchi State Revised Gender Policy",
         what="Guiding principles include gender mainstreaming, eliminating discrimination, sourcing human and financial capital, commitment to gender-responsive financing and budgeting, addressing social, economic and cultural determinants, scaling up female school enrollment, community reorientation, and empowerment schemes.",
         implementation="Information not readily available.",
         funding="Bauchi USAID.",
         source="https://ndcd.ng/activities/175"),

    dict(region="Sub-Saharan Africa", country="Nigeria", state="Multi-state", city="State-wide",
         lat=9.08, lng=8.68, type="Ordinance", year=2019, status="Passed", scope="Multi-state (Yobe and Borno States)",
         pilot_municipalities="Yobe State and Borno State",
         name="Protecting Women's Rights in the Sahel Region and Promoting Women's Leadership in Preventing Violent Extremism in Nigeria, Niger, Chad, and Mali",
         what="Emphasizes the protection of women's rights and promotion of women's leadership and contributions to addressing the current security crisis in the Sahel including violent extremism. Builds on existing capacities and past and ongoing initiatives. A critical component of UN Women's ongoing efforts to facilitate gender-responsive approaches to implementation of the UN Integrated Strategy for the Sahel.",
         implementation="Information not readily available.",
         funding="$245,000 USD in commitments.",
         source="https://ndcd.ng/activities/175"),

    dict(region="Sub-Saharan Africa", country="Nigeria", state="Multi-state", city="State-wide",
         lat=8.50, lng=7.50, type="Resolution", year=2018, status="Passed", scope="Multi-state (Kebbi, Niger, Taraba, Abia, Edo, Ogun States)",
         pilot_municipalities="Kebbi, Niger, Taraba, Abia, Edo, and Ogun States",
         name="Nigeria for Women Project",
         what="Supports improved livelihoods for benefiting women in targeted areas of Nigeria.",
         implementation="Information not readily available.",
         funding="$98,153,122 USD in commitments from the International Development Association.",
         source="https://ndcd.ng/activities/1359"),

    dict(region="Sub-Saharan Africa", country="Botswana", state="South East District", city="Gaborone",
         lat=-24.66, lng=25.91, type="Resolution", year=2024, status="Passed", scope="Nation-wide",
         name="DoD/Botswana Defence Force Women, Peace, and Security 5-Year Plan",
         what="Plan focused on sexual harassment and assault response and prevention, organizational reform, and social welfare including quality of life and health initiatives.",
         implementation="Information not readily available.",
         funding="Information not readily available.",
         source="https://www.dvidshub.net/news/478900/integrating-women-military-us-botswana-hold-women-peace-and-security-exchange-during-southern-accord"),

    dict(region="Sub-Saharan Africa", country="Nigeria", state="Bauchi State", city="State-wide",
         lat=10.50, lng=10.20, type="Ordinance", year=2022, status="Passed", scope="State-wide",
         name="Bauchi State Law to Prohibit All Forms of Violence Against Persons (VAPP)",
         what="Outlines consequences for certain violations of the law in terms of gender-based violence. Prohibits all forms of physical, sexual, psychological, domestic, political, and harmful traditional practices; discrimination against persons. Provides maximum protection and effective remedies for victims and punishment of offenders.",
         implementation="Information not readily available.",
         funding="Information not readily available.",
         source="https://judiciary.bu.gov.ng/uploads/legislations/BAUCHI%20STATE%20VAPP%202022.pdf"),

    dict(region="Sub-Saharan Africa", country="Kenya", state="Nairobi Province", city="Nairobi",
         lat=-1.29, lng=36.82, type="Ordinance", year=2023, status="Passed", scope="City",
         name="Nairobi City County Gender Mainstreaming Policy",
         what="Acts as a localized framework to implement Kenya's 2010 Constitutional mandate for gender equality, aiming to integrate gender-responsive approaches into county planning, budgeting, and service delivery. Focuses on addressing disparities, enhancing women's empowerment, and combating gender-based violence.",
         implementation="The policy mandates the use of gender-disaggregated data to guide decisions, ensuring that county projects—particularly in infrastructure and sanitation—address the specific needs of women and marginalized groups.",
         funding="Information not readily available.",
         source="https://nairobiassembly.go.ke/ncca/wp-content/uploads/paperlaid/2025/SESSIONAL-PAPER-NO.-1-OF-2025-ON-NAIROBI-CITY-COUNTY-GENDER-MAINSTREAMING-POLICY.pdf"),

    dict(region="Sub-Saharan Africa", country="Uganda", state="Kampala District", city="Kampala",
         lat=0.32, lng=32.58, type="Ordinance Draft", year=2021, status="Proposed - not yet passed", scope="City",
         name="Kampala Capital City (Prohibition and Prevention of Gender-Based Violence) Ordinance, 2021",
         what="Provides for the prohibition and prevention of and response to gender-based violence in Kampala. Bar, disco, video or film hall operators are banned from allowing individuals under 18 from accessing their premises. Fines and license revocation for those who defy the ordinance.",
         implementation="Proposed — not yet passed.",
         funding="Information not readily available.",
         source="https://ugandaradionetwork.net/story/-kcca-to-revoke-licenses-for-bars-that-admit-children"),

    dict(region="Sub-Saharan Africa", country="South Africa", state="Gauteng", city="Johannesburg",
         lat=-26.21, lng=28.03, type="Ordinance", year=2021, status="Passed", scope="City",
         name="City of Johannesburg Gender Policy",
         what="Developed to influence council plans, strategies, and programmes that foster gender equality in the City of Johannesburg. Provides guidelines for the removal of discriminatory barriers through gender-specific measures.",
         implementation="The Policy applies to all CoJ Departments and Municipal Entities (MEs), with the CoJ-DSD playing a leading role of coordination, facilitation, and management of certain policy processes.",
         funding="All CoJ departments and MEs must allocate adequate provision of their annual budget towards addressing disability and gender-related programmes.",
         source="https://joburg.org.za/documents_/Documents/POLICIES/Social%20Development/Gender%20Policy%20%20Final%20as%20at%2025%20August%202021.pdf"),

    dict(region="Sub-Saharan Africa", country="Ethiopia", state="Sidama Region", city="Hawassa",
         lat=7.05, lng=38.50, type="Declaration", year=2023, status="Passed", scope="City",
         name="The Quito Declaration: Global Commitment of Mayors to Accelerate Action — Safe Cities and Safe Public Spaces (Hawassa)",
         what="Concrete action that cities can take in support of gender equality and ending violence against women. Calls for increasing women's and girls' meaningful participation, leadership, and decision-making power in cities and communities.",
         implementation="Using partnerships to develop new, evidence-driven, and human rights-based approaches to prevent and respond to sexual harassment and other forms of violence against women and girls in public spaces.",
         funding="Information not readily available.",
         source="https://www.unwomen.org/en/news-stories/feature-story/2023/12/city-mayors-make-commitments-to-advance-action-on-gender-equality-globally"),

    dict(region="Sub-Saharan Africa", country="Niger", state="Capital Territory", city="Niamey",
         lat=13.49, lng=2.11, type="Declaration", year=2023, status="Passed", scope="City",
         name="The Quito Declaration: Global Commitment of Mayors to Accelerate Action — Safe Cities and Safe Public Spaces (Niamey)",
         what="Concrete action that cities can take in support of gender equality and ending violence against women. Calls for increasing women's and girls' meaningful participation, leadership, and decision-making power in cities and communities.",
         implementation="Using partnerships to develop new, evidence-driven, and human rights-based approaches to prevent and respond to sexual harassment and other forms of violence against women and girls in public spaces.",
         funding="Information not readily available.",
         source="https://www.unwomen.org/en/news-stories/feature-story/2023/12/city-mayors-make-commitments-to-advance-action-on-gender-equality-globally"),

    dict(region="Sub-Saharan Africa", country="Tanzania", state="Arusha Region", city="Arusha",
         lat=-3.39, lng=36.68, type="Declaration", year=2023, status="Passed", scope="City",
         name="The Quito Declaration: Global Commitment of Mayors to Accelerate Action — Safe Cities and Safe Public Spaces (Arusha)",
         what="Concrete action that cities can take in support of gender equality and ending violence against women. Calls for increasing women's and girls' meaningful participation, leadership, and decision-making power in cities and communities.",
         implementation="Using partnerships to develop new, evidence-driven, and human rights-based approaches to prevent and respond to sexual harassment and other forms of violence against women and girls in public spaces.",
         funding="Information not readily available.",
         source="https://www.unwomen.org/en/news-stories/feature-story/2023/12/city-mayors-make-commitments-to-advance-action-on-gender-equality-globally"),

    dict(region="Sub-Saharan Africa", country="Tanzania", state="Mjini Magharibi Region", city="Zanzibar City",
         lat=-6.17, lng=39.20, type="Declaration", year=2023, status="Passed", scope="City",
         name="The Quito Declaration: Global Commitment of Mayors to Accelerate Action — Safe Cities and Safe Public Spaces (Zanzibar City)",
         what="Concrete action that cities can take in support of gender equality and ending violence against women. Calls for increasing women's and girls' meaningful participation, leadership, and decision-making power in cities and communities.",
         implementation="Using partnerships to develop new, evidence-driven, and human rights-based approaches to prevent and respond to sexual harassment and other forms of violence against women and girls in public spaces.",
         funding="Information not readily available.",
         source="https://www.unwomen.org/en/news-stories/feature-story/2023/12/city-mayors-make-commitments-to-advance-action-on-gender-equality-globally"),

    dict(region="Sub-Saharan Africa", country="Uganda", state="Napak District", city="District-wide",
         lat=2.43, lng=34.33, type="LAP (Local Action Plan)", year=2024, status="Passed", scope="District-wide",
         name="LAP — Napak Local Action Plan",
         what="Signifies a pivotal moment in the district's commitment to promoting peace, gender equality, and inclusive development. Amplifies women's voices, safeguards peace, and supports communities to thrive in harmony.",
         implementation="Developed with key district stakeholders.",
         funding="Information not readily available.",
         source="https://wipc.org/napak-district-advances-women-peace-and-security-agenda-through-developing-local-action-plan/"),

    dict(region="Sub-Saharan Africa", country="Uganda", state="Kasese District", city="District-wide",
         lat=0.18, lng=30.08, type="LAP (Local Action Plan)", year=2021, status="Passed", scope="District-wide",
         name="LAP — Five Year Local Action Plan on Peace, Security, and Conflict Resolution (Kasese)",
         what="Developed at a time when Kasese district is considering community action as an alternative measure of dispute resolution, to manage and prevent conflicts at community and family levels. Promotes peaceful coexistence among the people of Kasese district.",
         implementation="Monitoring and evaluation plan integrated in the District Development Plan and council budget. Periodic assessments of implementation and performance evaluation.",
         funding="Information not readily available.",
         source="https://www.coact1325.org/wp-content/uploads/2022/01/DISTRICT-LAP-Kasese.pdf"),

    dict(region="Sub-Saharan Africa", country="Uganda", state="Adjumani District", city="District-wide",
         lat=3.25, lng=31.72, type="LAP (Local Action Plan)", year=2025, status="Passed", scope="District-wide",
         name="LAP — Adjumani District Local Action Plan on WPS",
         what="Aims to reduce all forms of conflicts and violence from 33% to 23%, reduce poverty from 38% to 28%, reduce GBV from 27% to 17%, and improve governance and service delivery from 71% to 95%. Implemented through 16 strategic interventions and 70 key activities.",
         implementation="Information not readily available.",
         funding="Financial help from the Women's International Peace Centre. Total budget of 19,785,000,000 shillings over 5 years.",
         source="https://adjumani.go.ug/adjumani-launches-5-year-local-action-plan-women-peace-and-security"),

    dict(region="Sub-Saharan Africa", country="Uganda", state="Yumbe District", city="District-wide",
         lat=3.47, lng=31.25, type="LAP (Local Action Plan)", year=2021, status="Passed", scope="District-wide",
         name="LAP — Yumbe District Local Action Plan on Prevention of All Forms of Conflict and Violence",
         what="Commitment to domesticate implementation of NAP III tailoring it to conflict issues in families and communities. Developed in a participatory process involving district and sub-county leaders, religious and cultural leaders, civil society organizations, teachers, and the media.",
         implementation="Progress monitored through quarterly reports.",
         funding="Allocated grand total of 3,716,099,500 shillings across 5 years.",
         source="https://www.coact1325.org/wp-content/uploads/2022/08/YUMBE-LAP-.pdf"),

    dict(region="Sub-Saharan Africa", country="Uganda", state="Kitgum District", city="District-wide",
         lat=3.28, lng=32.88, type="LAP (Local Action Plan)", year=2021, status="Passed", scope="District-wide",
         name="LAP — Five Year Local Action Plan on Ending All Forms of Conflicts and Violence (Kitgum)",
         what="Localizes the Uganda NAP III on UNSCR 1325 tailoring it to issues in families and communities in Kitgum district. Developed in a participatory manner involving all key stakeholders.",
         implementation="Implemented through police crime reports, district annual reports, LAP evaluation reports, and media reports.",
         funding="Allocated grand total of approximately 2,000,000,000 shillings for 5 years.",
         source="https://www.coact1325.org/wp-content/uploads/2022/08/KITGUM-LAP.pdf"),

    dict(region="Sub-Saharan Africa", country="Uganda", state="Amuria District", city="District-wide",
         lat=2.08, lng=33.67, type="LAP (Local Action Plan)", year=2021, status="Passed", scope="District-wide",
         name="LAP — Five Year Local Action Plan on Ending All Forms of Conflicts and Violence (Amuria)",
         what="Overall goal to have peaceful, empowered, and productive communities in Amuria District. Seven specific objectives including increased capacity of community groups accessing government programs, increased women and youth participation in leadership, and improved completion rate and quality of education.",
         implementation="Evaluated through district annual reports and LAP evaluation reports. Implemented through available funds, political will, and willingness of communities.",
         funding="Allocated grand total of 3,031,614,152 shillings for 5 years.",
         source="https://www.coact1325.org/wp-content/uploads/2022/08/AMURIA-LAP.pdf"),

    dict(region="Sub-Saharan Africa", country="Uganda", state="Kaberamaido District", city="District-wide",
         lat=1.78, lng=33.15, type="LAP (Local Action Plan)", year=2021, status="Passed", scope="District-wide",
         name="LAP — Five Year Local Action Plan for Ending All Forms of Conflicts and Violence (Kaberamaido)",
         what="Localizes the Uganda NAP on Women, Peace and Security tailoring it to address the conflicts in the district.",
         implementation="Monitored through District Annual Performance Reports, Annual Police Crime report, evaluation reports, and quarterly performance reports.",
         funding="Budget for 5 years: 1,033,229,000 shillings.",
         source="https://www.coact1325.org/wp-content/uploads/2022/08/KABERAMAIDO-LAP.pdf"),

    dict(region="Sub-Saharan Africa", country="Uganda", state="Luwero District", city="District-wide",
         lat=0.83, lng=32.50, type="LAP (Local Action Plan)", year=2021, status="Passed", scope="District-wide",
         name="LAP — District Local Action Plan on Women Peace and Security (Luwero)",
         what="First ever Local Action Plan of Luwero District, designed to achieve the District Vision of a vibrant, prosperous, socially and economically transformed community.",
         implementation="Reports will monitor progress. Implementation is based on available funds.",
         funding="4,362,748,000 shillings needed for 5 years.",
         source="https://www.coact1325.org/wp-content/uploads/2022/08/Luwero-LAP-.pdf"),

    dict(region="Sub-Saharan Africa", country="Uganda", state="Wakiso District", city="District-wide",
         lat=0.40, lng=32.48, type="LAP (Local Action Plan)", year=2025, status="Passed", scope="District-wide",
         name="LAP — Five Year Local Action Plan on Women, Peace, and Security (Wakiso)",
         what="Centers women in peace and security efforts, ensures their active participation in decision-making processes, and addresses the unique challenges they face. Integrates gender perspectives into security strategies and promotes inclusion of women in all spheres of peacebuilding.",
         implementation="Different reports will monitor progress.",
         funding="Total LAP budget: 3,366,250,000 shillings.",
         source="https://www.coact1325.org/wp-content/uploads/2025/07/Wakiso-District-Main-Local-Action-Plan-1-1.pdf"),

    dict(region="Sub-Saharan Africa", country="Kenya", state="Vihiga County", city="Mbale",
         lat=0.95, lng=34.33, type="Ordinance", year=2024, status="Passed", scope="County-wide",
         name="Vihiga County Sexual and Gender Based Violence Policy 2024",
         what="Seeks to establish a comprehensive response to SGBV and reinforce the county's commitment to protecting survivors, enhancing service delivery, and promoting gender equality.",
         implementation="With continued support from local and national partners, the policy sets a precedent for other counties in Kenya to follow in addressing this critical issue.",
         funding="Information not readily available.",
         source="https://vihiga.go.ke/sexual-gender-violence-and-children-protection-and-welfare-policies/"),

    dict(region="Sub-Saharan Africa", country="Kenya", state="Great Lakes Region", city="Nairobi",
         lat=-1.30, lng=36.83, type="RAP (Regional Action Plan)", year=2026, status="Passed", scope="Regional",
         name="RAP — Second Generation Regional Action Plan on Women, Peace, and Security (2026-2030)",
         what="Aims to strengthen women's leadership in peace processes, enhance regional cooperation, and improve coordination among member states in addressing cross-border security challenges.",
         implementation="Strong support from international partners including Germany. Capacity-building sessions on results-based monitoring and evaluation planned, bringing together government officials and civil society representatives.",
         funding="Information not readily available.",
         source="https://www.kenyanews.go.ke/kenya-commits-to-womens-peace-and-security/"),

    dict(region="Sub-Saharan Africa", country="Kenya", state="Great Lakes Region", city="Nairobi",
         lat=-1.31, lng=36.84, type="RAP (Regional Action Plan)", year=2018, status="Passed", scope="Regional",
         name="RAP — Regional Action Plan for the Implementation of United Nations Resolution 1325 (2000)",
         what="Facilitates a harmonized consideration of issues forming the basis of UNSCR 1325, providing an integrated Regional response to women, peace and security issues that transcend national boundaries. Consolidates gains made and fosters exchanges and mutual learning between ICGLR Member States.",
         implementation="The Executive Secretariat of the ICGLR was established and tasked with coordinating, facilitating, monitoring, and ensuring implementation of the Pact on Security, Stability and Development in the Great Lakes Region.",
         funding="Dedicated Special Fund with 15% of all available Funds established on Peace and Security allocated for WPS, as per UN standard.",
         source="https://wpsfocalpointsnetwork.org/wp-content/uploads/2021/07/ICGLR-1325-ACTION-PLAN.pdf"),

    dict(region="Sub-Saharan Africa", country="Nigeria", state="Plateau State", city="Jos North",
         lat=9.92, lng=8.88, type="LAP (Local Action Plan)", year=2017, status="Passed", scope="City",
         name="LAP — Local Action Plan on the Implementation of UNSCR 1325 (Jos North)",
         what="Developed with emphasis on prevention of conflict and encouraging the active and direct participation of women in conflict prevention, peacebuilding, and post-conflict efforts. Acknowledges the need for genuine engagement of civil society, including women-led organizations.",
         implementation="Core strategies include promotion and advocacy, legislation and policy, capacity building and service delivery, research documentation and dissemination, and coordination among stakeholders.",
         funding="Information not readily available.",
         source="https://wanepnigeria.org/jos-north-local-government-local-action-plan-lap/"),

    dict(region="Sub-Saharan Africa", country="Nigeria", state="Plateau State", city="Mangu",
         lat=9.38, lng=9.15, type="LAP (Local Action Plan)", year=2017, status="Passed", scope="City",
         name="LAP — Local Action Plan on the Implementation of UNSCR 1325 (Mangu)",
         what="Affirms the important role to be played by law enforcement agencies and other peacekeeping forces in ensuring the physical safety and security of women and girls from sexual and gender based violence in local communities. Addresses immediate and long-term needs of citizens before, during, and after conflict.",
         implementation="Uses the same implementation strategies as Jos North.",
         funding="Information not readily available.",
         source="https://wanepnigeria.org/mangu-localgovernment-local-action-plan-lap/"),

    dict(region="Sub-Saharan Africa", country="Nigeria", state="Benue State", city="Katsina-Ala",
         lat=7.17, lng=9.28, type="LAP (Local Action Plan)", year=2026, status="Ongoing", scope="City",
         name="LAP — Local Action Plan for Women, Peace, and Security (Katsina-Ala)",
         what="The Executive Chairman of Katsina-Ala Local Government Council inaugurated a seven-member committee on the Local Action Plan for Women, Peace and Security, reaffirming the Council's commitment to inclusive governance, peacebuilding, and community security.",
         implementation="Information not readily available.",
         funding="Information not readily available.",
         source="https://www.facebook.com/peverganathaniel.hency/posts/press-releasedr-shaku-inaugurates-committee-on-local-action-plan-lap-for-women-p/1705841870823109/"),

    # ── MENA ──────────────────────────────────────────────────────────────────
    dict(region="MENA", country="Yemen", state="Multi-governorate", city="Governorate-wide",
         lat=14.50, lng=46.00, type="LAP (Local Action Plan)", year=2024, status="Drafted", scope="Multi-governorate",
         pilot_municipalities="Aden, Abyan, Shabwa, Hadramout",
         name="LAP — Localization of WPS Project (Yemen)",
         what="Project includes mapping and analysis, localization workshops, local steering committees, and drafting of Local Action Plans across four governorates.",
         implementation="Information not readily available.",
         funding="Funded by the US Department of State Secretary's Office of Global Women's Issues.",
         source="https://www.peacetrackinitiative.org/en/projects/5"),

    dict(region="MENA", country="Syria", state="DAANES/Rojava", city="Region-wide",
         lat=36.51, lng=40.74, type="Ordinance", year=2023, status="Passed", scope="Region-wide",
         name="DAANES Social Contract",
         what="Contract for the newly autonomous regions in Northern Syria. For WPS it sets a 50% gender quota in all deliberative bodies and establishes women as equal parties to men.",
         implementation="Information not readily available.",
         funding="Information not readily available.",
         source="https://rojavainformationcenter.org/2023/12/aanes-social-contract-2023-edition/"),

    dict(region="MENA", country="Tunisia", state="Tunis Governorate", city="Tunis",
         lat=36.82, lng=10.17, type="Project", year=2020, status="Completed", scope="City",
         name="Femmedina Project (Tunis)",
         what="Gender-focused project that aims to rehabilitate and activate public spaces in the historic centre of Tunisian cities — the Medina — through a broader process of women's participation. Empowers women as participants in and architects of the Medina's rehabilitated public spaces.",
         implementation="More than 150 women and men engaged in a gender assessment of the Medina of Tunis, more than a dozen civil servants trained in inclusive urban governance, and seven public space interventions completed.",
         funding="USAID, Municipality of Tunis, Cities Alliance.",
         source="https://www.citiesalliance.org/femmedina-inclusive-city-programme"),

    dict(region="MENA", country="Tunisia", state="Sousse Governorate", city="Sousse",
         lat=35.83, lng=10.64, type="Project", year=2023, status="Completed", scope="City",
         name="Femmedina Project (Sousse)",
         what="Key priorities for neighborhood improvement including public safety, rehabilitation of the municipal market's degraded infrastructure, community engagement, and strengthening of local commercial activities.",
         implementation="500 citizens participated and contributed to identifying challenges women face in public spaces. More than 15 municipal members enhanced their expertise in gender-sensitive planning. Over 150 participants engaged in workshops.",
         funding="Swiss Agency for Development and Cooperation, CIDA.",
         source="https://www.citiesalliance.org/femmedina-inclusive-city-programme"),

    dict(region="MENA", country="Egypt", state="Cairo Governorate", city="Cairo",
         lat=30.04, lng=31.24, type="Prime Ministerial Decree", year=1994, status="Ongoing", scope="Nation-wide",
         name="Cairo International Center for Conflict Resolution, Peacekeeping, and Peacebuilding (CCCPA)",
         what="CCCPA's integrated and multidimensional approach to training covers: gender in conflict, the international and regional policy framework on WPS, integrating a gender perspective in peacemaking, peacekeeping and peacebuilding, and gender analysis tools.",
         implementation="Holds conferences with international organizations and training activities. Re-chartered in 2017.",
         funding="Information not readily available.",
         source="https://www.cccpa-eg.org/woman-peace"),

    dict(region="MENA", country="Saudi Arabia", state="Riyadh Governorate", city="Riyadh",
         lat=24.63, lng=46.72, type="Initiative", year=2025, status="Passed", scope="City",
         name="Basata Riyadh Initiative",
         what="Provides a vital platform to support female entrepreneurship and encourage participation from different groups. Offers women the opportunity to showcase handmade, innovative, and artisanal products to a wide audience.",
         implementation="Information not readily available.",
         funding="Information not readily available.",
         source="https://www.alriyadh.gov.sa/en/content/women-empowerment"),

    dict(region="MENA", country="Egypt", state="Damietta Governorate", city="Damietta",
         lat=31.42, lng=31.81, type="Declaration", year=2023, status="Passed", scope="City",
         name="The Quito Declaration — Safe Cities and Safe Public Spaces (Damietta)",
         what="Concrete action that cities can take in support of gender equality and ending violence against women. Calls for increasing women's and girls' meaningful participation, leadership, and decision-making power in cities and communities.",
         implementation="Investments in the safety and economic viability of public spaces including the redesign of the country's first market using an approach that creates a safe space for women vendors and customers.",
         funding="Information not readily available.",
         source="https://www.unwomen.org/en/news-stories/feature-story/2023/12/city-mayors-make-commitments-to-advance-action-on-gender-equality-globally"),

    dict(region="MENA", country="Morocco", state="Fez-Meknes", city="Fez",
         lat=34.02, lng=-5.01, type="Declaration", year=2023, status="Passed", scope="City",
         name="The Quito Declaration — Safe Cities and Safe Public Spaces (Fez)",
         what="Concrete action that cities can take in support of gender equality and ending violence against women. Calls for increasing women's and girls' meaningful participation, leadership, and decision-making power in cities and communities.",
         implementation="Using partnerships to develop new, evidence-driven, and human rights-based approaches to prevent and respond to sexual harassment and other forms of violence against women and girls in public spaces.",
         funding="Information not readily available.",
         source="https://www.unwomen.org/en/news-stories/feature-story/2023/12/city-mayors-make-commitments-to-advance-action-on-gender-equality-globally"),

    dict(region="MENA", country="Iraq", state="Kurdistan Region", city="Region-wide",
         lat=36.50, lng=44.00, type="RAP (Regional Action Plan)", year=2025, status="Passed", scope="Region-wide",
         name="RAP — Kurdistan Region Action Plan (2025-2030)",
         what="Model for collaboration and partnership to advance women's leadership, access to services and employment, and continued engagement in building lasting peace, recovery, and development.",
         implementation="Builds on the achievements of the previous plan. Strengthens institutional coordination, enhances policy frameworks, and places women's leadership at the center of peace and development efforts.",
         funding="Information not readily available.",
         source="https://arabstates.unwomen.org/en/stories/feature-story/2025/10/kurdistan-region-reaffirms-commitment-to-the-women-peace-and-security-agenda"),

    dict(region="MENA", country="Iraq", state="Kurdistan Region / Duhok Governorate", city="Duhok",
         lat=36.87, lng=42.99, type="LAP (Local Action Plan)", year=2024, status="Passed", scope="Governorate-wide",
         name="LAP — Localized Plan for 1325 Women, Peace, and Security (Duhok Governorate)",
         what="A call to action for all those committed to peace, security, and gender equality. Provides a roadmap for transformative change that uplifts women, strengthens communities, and promotes lasting peace.",
         implementation="Outlines programs and initiatives including a National Action Plan with budget listed out.",
         funding="Information not readily available.",
         source="https://govkrd.b-cdn.net/OtherEntities/High%20Council%20of%20Women%20Affairs/English/Publications/Plans/The%20Localised%20Plan%20for%201325%20%20Women%20%2C%20Peace%20%2C%20and%20Security%20Duhok%20Governorate.pdf"),

    dict(region="MENA", country="Turkey", state="Istanbul Province", city="Istanbul",
         lat=41.01, lng=28.97, type="LAP (Local Action Plan)", year=2021, status="Passed", scope="City",
         name="LAP — Local Equality Action Plan (Istanbul)",
         what="Local Equality Action Plans focus on gender equality while also taking into account the specialized needs of women who live in different conditions and have different problems and needs.",
         implementation="Has indicators for each goal so they can track progress. Outlines who is responsible for implementing and enforcing each goal.",
         funding="Mentions budgets throughout but no actual figures included in the plan.",
         source="https://uploads.ibb.istanbul/uploads/local_equality_action_plan_2021_2024_86c801f2c5.pdf"),

    dict(region="MENA", country="Israel", state="Tel Aviv District", city="Tel Aviv",
         lat=32.09, lng=34.78, type="LAP (Local Action Plan)", year=2022, status="Passed", scope="City",
         name="LAP — Fair Shared City: A Plan for Advancing Gender Equality in Tel Aviv-Yafo",
         what="Promotes the idea of routine and integral use of gender mainstreaming in the Municipality's operations. Assesses municipal processes, decisions, plans and operations from the perspective of women, and provides suitable solutions to advance gender equality.",
         implementation="Implemented over five years. Action items incorporated into municipal work plans and divided into three time spans: short (2021-2022), medium (2024), and long (2027).",
         funding="Information not readily available.",
         source="https://www.tel-aviv.gov.il/en/Documents/Introduction.pdf"),

    dict(region="MENA", country="Oman", state="Muscat Governorate", city="Muscat",
         lat=23.60, lng=58.58, type="Declaration", year=2024, status="Passed", scope="Nation-wide",
         name="Muscat Declaration on Progress in Implementation of the Beijing Declaration and Platform for Action in the Arab Region after Thirty Years",
         what="Reaffirms the Beijing Declaration, recommits to implementing it, and commends the progress made. Reiterates and plans the goals of WPS and actions towards its growth and implementation.",
         implementation="Information not readily available.",
         funding="Information not readily available.",
         source="https://arabstates.unwomen.org/en/stories/news/2024/12/muscat-declaration-on-progress-in-implementation-of-the-beijing-declaration-and-platform-for-action-in-the-arab-region-after-thirty-years"),

    dict(region="MENA", country="Algeria", state="Oran Province", city="Oran",
         lat=35.70, lng=-0.63, type="Project", year=2024, status="Completed", scope="City",
         name="Gender Approach in Local Urban Development Projects in Algeria",
         what="A project to promote gender in urban development through training and tools, a gendered approach, inclusive actions, communication media, dual gender approach, and exploratory walks.",
         implementation="Training of participants.",
         funding="Information not readily available.",
         source="https://www.giz.de/sites/default/files/media/pkb-document/2025-09/giz2024-en-urba-clima-gender-algeria.pdf"),

    dict(region="MENA", country="UAE", state="Abu Dhabi", city="Abu Dhabi",
         lat=24.45, lng=54.37, type="Initiative", year=2021, status="Passed", scope="Nation-wide",
         name="Sheikha Fatima bint Mubarak Women, Peace, and Security Centre of Excellence",
         what="The Centre is housed inside the General Women's Union complex in Abu Dhabi and offers a range of training courses locally and internationally. Participants engage in face-to-face courses combining presentations, interactive activities, and group discussions.",
         implementation="Information not readily available.",
         funding="Information not readily available.",
         source="https://arabstates.unwomen.org/en/news/stories/2021/06/sheikha-fatima-bint-mubarak-women-peace-and-security-centre-of-excellence-launched"),

    dict(region="MENA", country="Yemen", state="Aden Governorate", city="Aden",
         lat=12.79, lng=45.02, type="Action Plan", year=2023, status="Passed", scope="City",
         name="Gender Responsive Action Plan (Aden Police)",
         what="Aims to equip police personnel with gender-responsive knowledge and skills, improve access to data, empower officers to conduct investigations effectively, and build trust between police and the communities they serve.",
         implementation="Trains male and female officers to make security institutions more inclusive. Includes provision of computer equipment for twenty police stations in Aden, rehabilitation of facilities, and installation of separate washroom facilities, air ventilators, and solar energy systems.",
         funding="Information not readily available.",
         source="https://www.undp.org/arab-states/stories/women-police-aden-support-access-justice-yemen"),

    dict(region="MENA", country="Jordan", state="Jerash Governorate", city="Jerash",
         lat=32.27, lng=35.90, type="Unit", year=2020, status="Passed", scope="City",
         name="Women Empowerment Unit (Jerash)",
         what="Women's Economic Empowerment Units to support determining local gender priorities and advocating for women's concerns.",
         implementation="Conducting continuous assessment of women's needs in Jerash. Facilitating implementation of programs and projects dealing with women.",
         funding="Information not readily available.",
         source="https://jordan.un.org/sites/default/files/2022-10/Establishment%20of%20WEE%20UNITS%20REPORT%20UNDP%207%20June.pdf"),

    dict(region="MENA", country="Tunisia", state="Sousse Governorate", city="Enfidha",
         lat=36.13, lng=10.38, type="Commission", year=2019, status="Passed", scope="City",
         name="Gender Equality and Parity Commission (Enfidha)",
         what="Improves and develops the economic, scientific, cultural, social, sports, and recreational life of both men and women. Improves the status of women and defends their rights, especially rural women, widows, single women, and formerly incarcerated women.",
         implementation="Improves equal employment opportunities, provides social support to women, and organizes awareness-raising seminars and campaigns on women and gender equality.",
         funding="Information not readily available.",
         source="https://www.euromedwomen.foundation/pg/en/profile/ermwf.yomiti40"),

    dict(region="MENA", country="Morocco", state="Guelmim Province", city="Guelmim",
         lat=28.99, lng=-10.06, type="Commission", year=2019, status="Passed", scope="City",
         name="Equity, Parity, and Gender Mainstreaming Commission of Guelmim",
         what="A participatory mechanism for dialogue and consultation enabling elected council members to continuously communicate with citizens and civil society. Advocates integrating and enabling women's participation in local development programs.",
         implementation="Organizes training activities and networking meetings with civil and elected actors within the framework of participatory democracy.",
         funding="Information not readily available.",
         source="https://www.euromedwomen.foundation/pg/en/profile/ermwf.lefamu811"),

    dict(region="MENA", country="Jordan", state="Irbid Governorate", city="Irbid",
         lat=32.56, lng=35.85, type="Project", year=2025, status="Passed", scope="City",
         name="Economic Support for Women and Achieving Sustainable Economic Protection (Irbid)",
         what="Aims to equip Jordanians with the tools to contribute to their country's progress and secure a better standard of living. Addresses economic, social, legal, and political challenges women face in different communities.",
         implementation="Information not readily available.",
         funding="Funded by the Regional Development and Protection Program in Irbid Governorate.",
         source="https://www.petra.gov.jo/Include/InnerPage.jsp?ID=67378&lang=en&name=en_news"),
]

TYPE_COLORS = {
    "Ordinance":       "#c2185b",
    "Resolution":      "#00897b",
    "Law":             "#f57f17",
    "Regulation":      "#5c35cc",
    "Motion":          "#e65100",
    "Act":             "#0077b6",
    "Amendment":       "#7b2d8b",
    "Framework":       "#2d6a4f",
    "Initiative":      "#e76f51",
    "Plan":            "#457b9d",
    "Program":         "#e9c46a",
    "Sub-Decree":      "#264653",
    "Approved Strategy": "#6d6875",
    "Municipal Agreement": "#a8763e",
    "Municipal Plan":      "#2196f3",
    "UN Initiative":       "#009688",
    "Action Plan":         "#795548",
    "LAP (Local Action Plan)":    "#1565c0",
    "RAP (Regional Action Plan)": "#6a1b9a",
    "Declaration":                "#00838f",
    "Ordinance Draft":            "#9e9e9e",
    "Prime Ministerial Decree":   "#37474f",
    "Commission":                 "#558b2f",
    "Unit":                       "#ad1457",
    "Executive Order": "#b71c1c",
    "Other":           "#666666",
}

ALL_REGIONS = [
    "All Regions",
    "EA (East Asia)",
    "NA (North America)",
    "SSEA (South & Southeast Asia)",
    "Latin America",
    "Oceania",
    "Western Europe",
    "Eastern Europe",
    "MENA",
    "Sub-Saharan Africa",
]

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🌍 Global Policy Tracker")
    st.markdown("*Women's rights policies worldwide*")
    st.markdown("---")

    selected_region = st.selectbox("Region", ALL_REGIONS)

    year = st.slider("Show policies passed by:", 1960, 2026, 2026)

    st.markdown("**Policy Type**")
    all_types = sorted(set(p["type"] for p in policies))
    active_types = []
    for t in all_types:
        if st.checkbox(t, value=True, key=f"type_{t}"):
            active_types.append(t)

    st.markdown("---")
    def clear_search():
        st.session_state["search"] = ""

    if "search" not in st.session_state:
        st.session_state["search"] = ""

    search = st.text_input("Search", placeholder="policy, city, country...", key="search")
    if st.session_state["search"]:
        st.button("✕ Clear search", on_click=clear_search)

# ── FILTER ────────────────────────────────────────────────────────────────────
filtered = [
    p for p in policies
    if p["year"] <= year
    and p["type"] in active_types
    and (selected_region == "All Regions" or p.get("region") == selected_region)
    and (st.session_state.get("search", "") == "" or
         st.session_state.get("search", "").lower() in p["name"].lower() or
         st.session_state.get("search", "").lower() in p["country"].lower() or
         st.session_state.get("search", "").lower() in p["city"].lower())
]

# ── HEADER ────────────────────────────────────────────────────────────────────
st.markdown("# 🌍 Global Policy Tracker")
st.markdown("*Women's rights ordinances, resolutions & laws worldwide*")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f'<div class="stat-box"><div class="stat-num">{len(filtered)}</div><div class="stat-label">Policies Shown</div></div>', unsafe_allow_html=True)
with col2:
    this_year_count = len([p for p in filtered if p["year"] == year])
    st.markdown(f'<div class="stat-box"><div class="stat-num">{this_year_count}</div><div class="stat-label">Passed in {year}</div></div>', unsafe_allow_html=True)
with col3:
    n_countries = len(set(p["country"] for p in filtered))
    st.markdown(f'<div class="stat-box"><div class="stat-num">{n_countries}</div><div class="stat-label">Countries</div></div>', unsafe_allow_html=True)
with col4:
    n_regions = len(set(p["region"] for p in filtered))
    st.markdown(f'<div class="stat-box"><div class="stat-num">{n_regions}</div><div class="stat-label">Regions</div></div>', unsafe_allow_html=True)

st.markdown("---")

# ── MAP ───────────────────────────────────────────────────────────────────────
import math

region_centers = {
    "EA (East Asia)":                [35, 115],
    "NA (North America)":            [45, -95],
    "SSEA (South & Southeast Asia)": [15, 100],
    "Latin America":                 [-15, -60],
    "Oceania":                       [-25, 145],
    "Western Europe":                [50, 10],
    "Eastern Europe":                [52, 30],
    "MENA":                          [25, 40],
    "Sub-Saharan Africa":            [-5, 25],
}
zoom_levels = {
    "All Regions": 2,
    "EA (East Asia)": 4,
    "NA (North America)": 3,
    "SSEA (South & Southeast Asia)": 4,
    "Latin America": 3,
    "Oceania": 4,
    "Western Europe": 4,
    "Eastern Europe": 4,
    "MENA": 4,
    "Sub-Saharan Africa": 3,
}
center = region_centers.get(selected_region, [20, 10])
zoom = zoom_levels.get(selected_region, 2)

m = folium.Map(location=center, zoom_start=zoom, tiles="CartoDB positron", prefer_canvas=True)

# Jitter overlapping dots
placed = []
def get_jittered(lat, lng):
    THRESH = 1.0
    nearby = [pos for pos in placed if math.sqrt((pos[0]-lat)**2 + (pos[1]-lng)**2) < THRESH]
    if not nearby:
        placed.append((lat, lng))
        return lat, lng
    n = len(nearby) + 1
    angle = (n - 1) * (2 * math.pi / max(n, 4)) - math.pi / 2
    radius = 0.7
    jlat = lat + radius * math.cos(angle)
    jlng = lng + radius * math.sin(angle)
    placed.append((jlat, jlng))
    return jlat, jlng

for p in filtered:
    color = TYPE_COLORS.get(p["type"], "#666")
    is_new = p["year"] == year
    radius = 10 if is_new else 7
    jlat, jlng = get_jittered(p["lat"], p["lng"])

    scope_html = f'<span style="color:#c2185b; font-size:10px;">📍 {p["scope"]}</span>&nbsp;·&nbsp;' if p.get("scope") else ""

    popup_html = f"""
    <div style="font-family: -apple-system, sans-serif; width: 300px; padding: 6px;">
        <div style="font-size: 13px; font-weight: 700; color: {color}; margin-bottom: 6px; line-height: 1.4;">
            {p['name']}
        </div>
        <div style="font-size: 11px; color: #666; margin-bottom: 10px;">
            {scope_html}
            <span style="background:{color}22; border:1px solid {color}; border-radius:10px;
                         padding:1px 8px; font-size:10px; color:{color}; font-weight:600;">{p['type']}</span>
            &nbsp;·&nbsp; {p['city']}, {p.get('state','')}, {p['country']}
            &nbsp;·&nbsp; <b>{p['year']}</b>
        </div>
        <div style="font-size: 10px; color: #aaa; font-weight: 700; text-transform: uppercase;
                    letter-spacing: 0.08em; margin-bottom: 3px;">What is the policy?</div>
        <div style="font-size: 11px; color: #444; line-height: 1.6; margin-bottom: 10px;">{p['what']}</div>
        {'<div style="font-size: 10px; color: #aaa; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 3px;">Pilot Municipalities</div><div style="font-size: 11px; color: #444; line-height: 1.6; margin-bottom: 10px;">' + p['pilot_municipalities'] + '</div>' if p.get('pilot_municipalities') else ''}
        <div style="font-size: 10px; color: #aaa; font-weight: 700; text-transform: uppercase;
                    letter-spacing: 0.08em; margin-bottom: 3px;">Implementation</div>
        <div style="font-size: 11px; color: #444; line-height: 1.6; margin-bottom: 10px;">{p['implementation']}</div>
        <div style="font-size: 10px; color: #aaa; font-weight: 700; text-transform: uppercase;
                    letter-spacing: 0.08em; margin-bottom: 3px;">Funding</div>
        <div style="font-size: 11px; color: #444; line-height: 1.6; margin-bottom: 12px;">{p['funding']}</div>
        <a href="{p['source']}" target="_blank"
           style="display:inline-block; background:{color}; color:white; padding:6px 14px;
                  border-radius:4px; font-size:11px; font-weight:600; text-decoration:none;">
           ↗ View Source
        </a>
    </div>
    """

    folium.CircleMarker(
        location=[jlat, jlng],
        radius=radius,
        color="white",
        weight=2,
        fill=True,
        fill_color=color,
        fill_opacity=1.0 if is_new else 0.85,
        popup=folium.Popup(popup_html, max_width=330),
        tooltip=f"{p['name'][:55]}{'...' if len(p['name'])>55 else ''} · {p['year']}",
    ).add_to(m)

st_folium(m, width="100%", height=520, returned_objects=[])

# ── EXPORT MAP AS HTML ────────────────────────────────────────────────────────
st.markdown("---")
col_exp1, col_exp2 = st.columns([2, 1])
with col_exp1:
    st.markdown("**📥 Export Map**")
    st.caption("Download the map as a standalone HTML file you can open in any browser, zoom to your liking, and screenshot for the poster.")
with col_exp2:
    map_html = m._repr_html_()
    full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <title>Global Policy Tracker</title>
    <style>
        body {{ margin: 0; padding: 0; background: #f5f5f0; font-family: Georgia, serif; }}
        h1 {{ text-align: center; color: #c2185b; padding: 16px 0 4px; margin: 0; font-size: 2rem; }}
        p {{ text-align: center; color: #888; margin: 0 0 8px; font-size: 0.9rem; }}
        #map {{ width: 100%; height: calc(100vh - 90px); }}
    </style>
</head>
<body>
    <h1>Global Policy Tracker</h1>
    <p>Women's rights ordinances, resolutions & laws worldwide</p>
    {map_html}
</body>
</html>"""
    st.download_button(
        label="⬇ Download Map (HTML)",
        data=full_html,
        file_name="policy_map.html",
        mime="text/html",
    )

# ── POLICY LIST ───────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(f"### All Policies ({len(filtered)})")

for p in sorted(filtered, key=lambda x: (-x["year"], x["country"])):
    color = TYPE_COLORS.get(p["type"], "#666")
    with st.expander(f"**{p['name'][:80]}{'...' if len(p['name'])>80 else ''}** — {p['city']}, {p['country']} ({p['year']})"):
        col_a, col_b = st.columns([1, 3])
        with col_a:
            st.markdown(f"**Type:** {p['type']}")
            st.markdown(f"**Year:** {p['year']}")
            st.markdown(f"**Status:** {p['status']}")
            if p.get("scope"):
                st.markdown(f"**Scope:** {p['scope']}")
            if p.get("pilot_municipalities"):
                st.markdown(f"**Pilot Municipalities:** {p['pilot_municipalities']}")
            st.markdown(f"**Region:** {p.get('region','')}")
            st.markdown(f"**Location:** {p['city']}, {p.get('state','')}, {p['country']}")
        with col_b:
            st.markdown(f"**What is the policy?**")
            st.markdown(p["what"])
            st.markdown(f"**Implementation**")
            st.markdown(p["implementation"])
            st.markdown(f"**Funding**")
            st.markdown(p["funding"])
            st.markdown(f"[↗ View Source]({p['source']})")
