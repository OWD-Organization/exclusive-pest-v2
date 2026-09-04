# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from services import *

CITIES = ["Phoenix","Scottsdale","Mesa","Chandler","Gilbert","Glendale","Peoria","Surprise",
          "Tempe","Fountain Hills","Cave Creek","Goodyear","Buckeye","Queen Creek",
          "San Tan Valley","Maricopa","Casa Grande"]

body = (
hero(
  kick="Arizona Bark Scorpion Specialists",
  h1="Scorpion control in Phoenix, AZ. Targeted treatment that lasts.",
  paras=[
    "The Arizona bark scorpion is the most venomous scorpion in North America, and one of "
    "the most common uninvited guests in Phoenix Valley homes. A generic pest spray won't "
    "solve the problem."],
  cta_label="Schedule my scorpion evaluation",
  plate="Most venomous scorpion in North America",
  img="build-assets/service-scorpion-stock.jpg",
  alt="An Arizona bark scorpion on desert gravel, tail raised.", w=800, h=600)
+ C.ACTIONBAR +
f'''
<!-- ===================== LA AMENAZA ===================== -->
<section class="band band--2 pad seam-host">
  <div class="shell">
{head_block("The threat", "Why scorpions are a serious problem in the Phoenix Valley",
  "The Arizona bark scorpion thrives in the desert climate of Maricopa and Pinal County. "
  "Unlike most pests, scorpions are uniquely equipped to invade homes, and uniquely "
  "difficult to remove without a targeted strategy.")}
{cards([
  dict(h="Nocturnal", body="Active at night, making infestations easy to miss."),
  dict(h="Excellent climbers", body="Capable of scaling stucco walls and slipping through gaps as thin as a credit card."),
  dict(h="Highly venomous", body="The only U.S. scorpion species whose venom can cause severe medical reactions."),
  dict(h="Drawn to moisture", body="Kitchens, bathrooms, and garages are common entry points."),
], tight=True,
  note="Homes near desert washes, open lots, or block wall fencing are particularly "
       "vulnerable, but scorpions can enter any property in the valley.")}
  </div>
{C.cactus('seam')}</section>

<!-- ===================== PROCESO ===================== -->
<section class="band pad">
  <div class="shell">
{head_block("How we work", "Our scorpion control process",
  "Four stages. Each grounded in scorpion biology and Arizona-specific harborage patterns, "
  "not a generic spray schedule.", tagmod=" tag--orange")}
{steps([
  ("Property Evaluation",
   "Thorough inspection of your home's exterior, perimeter, and entry points. We identify "
   "harborage zones and the specific conditions attracting scorpions."),
  ("Custom Treatment Plan",
   "Using targeted knowledge of bark scorpion biology, we build a plan specific to your "
   "property, addressing the scorpions present and the conditions attracting more."),
  ("Exclusion &amp; Treatment",
   "We seal key entry points and treat your home's perimeter, block walls, and harborage "
   "zones with products designed to disrupt scorpion biology, not just repel temporarily."),
  ("Follow-Up &amp; Monitoring",
   "Lasting scorpion control requires ongoing vigilance. We track treatment performance and "
   "adjust through every season to keep your home protected."),
])}
  </div>
</section>

<!-- ===================== ZONAS ===================== -->
<section class="band band--paper pad">
  <div class="shell">
{head_block("Service areas", "Scorpion control across the Phoenix Valley",
  "We provide scorpion elimination and prevention services throughout Maricopa and Pinal County.",
  tagmod=" tag--cactus")}
{areas(CITIES)}
  </div>
</section>

<!-- ===================== FAQ ===================== -->
<section class="band pad faq-host">
  <div class="shell">
{head_block("FAQ", "Frequently asked questions",
  "Everything Phoenix Valley homeowners ask about scorpion control.")}
{faq([
 ("How do I know if I have a scorpion infestation?",
  "The most common signs are direct sightings, typically at night near baseboards, in closets, "
  "under furniture, or along exterior walls. A UV blacklight flashlight will cause scorpions to "
  "glow a bright green in the dark, making nighttime inspections more effective. If you're "
  "finding scorpions regularly inside your home, it's a sign the problem needs professional treatment."),
 ("Are Arizona bark scorpions really dangerous?",
  "Yes. The Arizona bark scorpion is the only scorpion in the U.S. whose sting can cause severe "
  "symptoms, including intense pain, numbness, and in vulnerable individuals (children, the "
  "elderly, or those with allergies), potentially serious reactions. Prompt professional "
  "treatment is strongly recommended if you find them inside your home."),
 ("Why do I keep finding scorpions even after spraying myself?",
  "Scorpions have a unique biology that makes over-the-counter sprays largely ineffective. Their "
  "metabolism is slow, they absorb little product through their exoskeleton, and they rarely come "
  "into contact with treated surfaces long enough for a general spray to work. Effective scorpion "
  "control requires targeted application methods and products specifically chosen for scorpion biology."),
 ("How long does scorpion treatment take to work?",
  "Most clients notice a significant reduction in scorpion activity within the first 2 to 4 weeks "
  "following an initial treatment. Complete elimination of an infestation typically requires "
  "consistent follow-up treatment cycles, as new scorpions can move in from surrounding areas or "
  "neighboring properties."),
 ("Is your scorpion treatment safe for my kids and pets?",
  "Yes. We select every product with family and pet safety as a primary consideration. We'll walk "
  "you through what's being applied, how long to stay off treated surfaces, and what precautions "
  "to take, so you always know exactly what's happening in your home."),
 ("Do you offer scorpion control near Scottsdale and Cave Creek?",
  "Yes, we serve the entire Phoenix Valley, including Scottsdale, Cave Creek, Fountain Hills, and "
  "all surrounding communities. These areas are among the highest-activity scorpion zones in the "
  "valley, and we have significant experience treating properties throughout the north and east valley."),
])}
  </div>
  <img class="faq-owl" src="build-assets/owl-mark.png" alt="" width="448" height="425" loading="lazy" aria-hidden="true">
  <picture class="cactus faq-cactus">
    <source srcset="build-assets/cactus-mark2.webp" type="image/webp">
    <img src="build-assets/cactus-mark2.png" alt="" width="520" height="737" loading="lazy" aria-hidden="true">
  </picture>
</section>
'''
+ C.cta("Get a scorpion plan built for your property.",
        "Every evaluation is on-site, no obligation, and tailored to your home. "
        "Phoenix Valley, Maricopa and Pinal County.")
)

print(page("scorpion-control.html",
  "Scorpion Control Phoenix AZ | Arizona Bark Scorpion Specialists",
  "Arizona bark scorpion control across the Phoenix Valley. IPM approach targeting scorpion "
  "biology and harborage, not a generic spray. Licensed, wildlife-conscious, family-safe.",
  [("Home","index.html"),("Services","index.html#services"),("Scorpion Control",None)],
  body, "scorpion"))
