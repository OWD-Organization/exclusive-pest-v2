# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from services import *

CITIES = ["Phoenix","Scottsdale","Mesa","Chandler","Gilbert","Glendale","Tempe","Peoria",
          "Surprise","Queen Creek","San Tan Valley","Fountain Hills","Cave Creek",
          "Goodyear","Maricopa"]

SPECIES = [
  dict(tag="Aggressive", tagmod=" card-tag--orange", h="Fire Ants", tone=" card--gold",
       body="Territorial and capable of delivering a painful sting. Valley colonies can number "
            "in the hundreds of thousands and spread rapidly."),
  dict(tag="Structural", h="Carpenter Ants", tone="",
       body="Unlike most ants, they tunnel through wood to build their nests, causing structural "
            "damage over time. Often mistaken for termites."),
  dict(tag="Perimeter", h="Pavement Ants", tone=" card--sky",
       body="Typically found along driveways, sidewalks, and foundations. Less aggressive but "
            "highly invasive inside the home."),
  dict(tag="Supercolony", h="Argentine Ants", tone="",
       body="One of the most common home-invading ants in Arizona. They form massive "
            "supercolonies and are highly resistant to generic treatments."),
  dict(tag="Indoor trail", h="Odorous House Ants", tone=" card--gold",
       body="Small, fast, and persistent. Emit a distinct odor when crushed. Often trail through "
            "kitchens and bathrooms in large numbers."),
  dict(h="Not sure which one?", tone=" card--cactus",
       body="We identify the species on-site before any product is applied. Identification "
            "drives the treatment plan.",
       link="Book an identification visit", href="#contact"),
]

body = (
hero(
  kick="Ant Elimination &amp; Prevention",
  h1="Ant control in Phoenix, AZ. Targeted solutions for every species.",
  paras=[
    "Ants are among the most persistent pests in the Phoenix Valley, and one of the most "
    "mishandled. A generic spray may knock back the workers you see, but the colony behind "
    "your walls keeps growing."],
  cta_label="Get my ant control quote",
  plate="Species identified on-site before any product is applied",
  img="build-assets/service-scorpion.jpg",
  alt="Bait stations staged on a Phoenix Valley driveway before a perimeter treatment.",
  w=600, h=600)
+ C.ACTIONBAR +
f'''
<!-- ===================== ESPECIES ===================== -->
<section class="band band--2 pad seam-host" id="species">
  <div class="shell">
{head_block("Know your invader", "Common ant species in the Phoenix Valley",
  "Each species requires a different strategy. Identification is step one.")}
{cards(SPECIES)}
    <p class="slab reveal">We treat the colony, not the symptom.</p>
  </div>
{C.cactus('seam')}</section>

<!-- ===================== ENFOQUE ===================== -->
<section class="band pad" id="method">
  <div class="shell split">
    <div class="stack reveal" style="--s:1.35rem">
      <div>
        <span class="tag tag--orange">Our approach</span>
        <h2 style="font-size:var(--step-3)">Why generic spraying makes ant problems worse</h2>
      </div>
      <div class="prose">
        <p>Over-the-counter sprays kill the workers you see but signal danger to the colony,
        causing it to split and relocate. One ant problem becomes several.</p>
        <p>Our process starts with inspection: species identification, trail mapping, entry point
        assessment, and conditions analysis. From there, we apply species-specific baits,
        perimeter barriers, and nest-directed products that eliminate the colony at the source.</p>
      </div>
    </div>
    <div class="split-media reveal" style="--d:120ms">
      <div class="blk">
        <h3 style="font-size:var(--step-1);margin-bottom:0.3rem">What that looks like on site</h3>
        <ul class="ticks">
          <li><b>Species-specific baits</b>, chosen for the colony you actually have</li>
          <li><b>Perimeter barriers</b>, stop the trail at the property line</li>
          <li><b>Nest-directed products</b>, eliminate the colony, not just the surface</li>
          <li><b>Environmental advisory</b>, what's attracting them and how to break the cycle</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ===================== ZONAS ===================== -->
<section class="band band--paper pad">
  <div class="shell">
{head_block("Service areas", "Ant control across the Phoenix Valley",
  "We provide ant elimination and prevention services throughout Maricopa and Pinal County.",
  tagmod=" tag--cactus")}
{areas(CITIES)}
  </div>
</section>

<!-- ===================== FAQ ===================== -->
<section class="band pad faq-host">
  <div class="shell">
{head_block("FAQ", "Frequently asked questions",
  "Everything Phoenix Valley homeowners ask about ant control.")}
{faq([
 ("Why do I suddenly have ants inside my home?",
  "Ants typically enter homes in search of food, water, or shelter, often triggered by temperature "
  "changes, rainfall, or drought. In the Phoenix Valley, ant activity spikes in spring and after "
  "monsoon season. If you're seeing trails indoors, the colony has likely found a reliable food or "
  "water source nearby."),
 ("Why did spraying ant killer make things worse?",
  "Over-the-counter sprays kill the workers you see but signal danger to the colony, causing it to "
  "split and relocate, a process called budding. This can turn one ant problem into several. "
  "Professional treatments use species-specific baits and nest-directed products that eliminate "
  "the colony itself."),
 ("How long does ant treatment take to work?",
  "Bait-based treatments typically work within 1 to 2 weeks as workers carry the product back to "
  "the colony. Perimeter and barrier treatments provide more immediate protection. We'll set "
  "expectations based on the specific species and infestation level at your property."),
 ("Are your ant treatments safe around food prep areas?",
  "Yes. We use products appropriate for indoor use and will guide you on any precautions for "
  "kitchens and food storage areas before and after treatment."),
 ("Do you treat fire ant mounds in the yard?",
  "Yes, outdoor fire ant mounds are included in our property treatment. We address both interior "
  "trails and exterior colonies for complete coverage."),
])}
  </div>
  <img class="faq-owl" src="build-assets/owl-mark.png" alt="" width="448" height="425" loading="lazy" aria-hidden="true">
  <picture class="cactus faq-cactus">
    <source srcset="build-assets/cactus-mark2.webp" type="image/webp">
    <img src="build-assets/cactus-mark2.png" alt="" width="520" height="737" loading="lazy" aria-hidden="true">
  </picture>
</section>
'''
+ C.cta("Stop the trail at your property line.",
        "Every evaluation is on-site, no obligation, and tailored to the species invading your home.")
)

print(page("ant-control.html",
  "Ant Control Phoenix AZ | Targeted Solutions for Every Species",
  "Ant control across the Phoenix Valley. We identify the species, locate the nest and eliminate "
  "the colony at its source with species-specific baits. Licensed in Arizona.",
  [("Home","index.html"),("Services","index.html#services"),("Ant Control",None)],
  body, "ant"))
