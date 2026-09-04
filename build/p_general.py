# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from services import *

CITIES = ["Phoenix","Scottsdale","Mesa","Chandler","Gilbert","Glendale","Peoria","Surprise",
          "Tempe","Fountain Hills","Cave Creek","Goodyear","Buckeye","Queen Creek",
          "San Tan Valley","Apache Junction","Maricopa","Casa Grande","Florence"]

PESTS = [
  dict(h="Scorpions",   body="Arizona bark scorpion elimination and prevention.",
       tag="Featured", tagmod=" card-tag--orange", tone=" card--gold"),
  dict(h="Ants",        body="Fire, carpenter, Argentine, odorous house ants.",
       tag="Featured", tagmod=" card-tag--orange", tone=" card--gold"),
  dict(h="Spiders",     body="Black widow, brown recluse, common house spiders.",
       tone=""),
  dict(h="Cockroaches", body="German, American, and Turkestan cockroaches.",
       tone=""),
  dict(h="Crickets",    body="Perimeter and interior cricket management.", tone=" card--sky"),
  dict(h="Silverfish",  body="Targeted treatments for moisture-driven infestations.", tone=""),
  dict(h="Earwigs",     body="Harborage treatment and entry point exclusion.", tone=" card--sky"),
  dict(h="Mosquitoes",  body="Breeding site treatment and adult population control.", tone=""),
  dict(h="Bees &amp; Wasps", body="Hive and nest removal, cavity treatment.", tone=" card--sky"),
  dict(h="And more",    body="If it's in the Phoenix Valley, we've treated it.", tone=""),
]

body = (
hero(
  kick="Comprehensive Home Pest Protection",
  h1="General pest control in Phoenix, AZ. One plan for every pest.",
  paras=[
    "The Phoenix Valley has a pest profile unlike anywhere else. Year-round warm temperatures, "
    "monsoon cycles, and desert proximity create ideal conditions for a wide range of insects, "
    "and no single pest exists in isolation."],
  cta_label="Get my general pest control plan",
  plate="One custom treatment plan. Complete coverage. No shortcuts.",
  img="build-assets/service-general.jpg",
  alt="Wire mesh exclusion fitted over a wall opening during a general pest treatment.",
  w=600, h=600)
+ C.ACTIONBAR +
f'''
<!-- ===================== COBERTURA ===================== -->
<section class="band band--2 pad seam-host" id="coverage">
  <div class="shell">
{head_block("What we cover", "Complete Valley pest coverage",
  "Every common pest in the Phoenix Valley, handled under one custom plan.")}
{cards(PESTS, tight=True)}
    <p class="slab reveal">Custom plans, not route schedules.</p>
  </div>
{C.cactus('seam')}</section>

<!-- ===================== METODO ===================== -->
<section class="band pad" id="method">
  <div class="shell">
{head_block("Our method", "Why Integrated Pest Management delivers better results",
  "Generic pest control companies apply the same broad-spectrum spray to every home on the "
  "route. It suppresses surface activity temporarily, and does little else.",
  tagmod=" tag--orange")}
    <p class="prose reveal" style="margin-top:1rem;font-weight:800;color:var(--fg)">Before any product is applied, we evaluate:</p>
{steps([
  ("What's present, and exactly which species",
   "Identification drives the entire treatment plan."),
  ("Where they enter and what attracts them",
   "Entry points, harborage zones, and environmental triggers."),
  ("What's sustaining the infestation",
   "Conditions feeding the colony, not just surface symptoms."),
  ("The plan to solve it for good",
   "Products, methods, and timing chosen for your property."),
])}
  </div>
</section>

<!-- ===================== SEGURIDAD ===================== -->
<section class="band band--paper pad" id="safe">
  <div class="shell split">
    <div class="stack reveal" style="--s:1.35rem">
      <div>
        <span class="tag tag--cactus">Safe for what matters</span>
        <h2 style="font-size:var(--step-3)">Garden-safe and family-safe treatments</h2>
      </div>
      <div class="prose">
        <p>We believe thorough pest control and household safety are not in conflict. Every product
        we apply is carefully selected to ensure it's safe for children, pets, and, where
        applicable, your vegetable garden and landscaping.</p>
        <p>We'll walk you through what's being used in your home, why it was chosen, and what to expect.</p>
      </div>
    </div>
    <div class="split-media reveal" style="--d:120ms">
      <div class="cards" style="margin-top:0;grid-template-columns:repeat(2,minmax(0,1fr))">
      <article class="card"><h3>Child-safe</h3><p>Toys moved before treatment.</p></article>
      <article class="card card--gold"><h3>Pet-safe</h3><p>Bowls removed before product is applied.</p></article>
      <article class="card card--sky"><h3>Garden-safe</h3><p>Vegetable beds and landscaping protected.</p></article>
      <article class="card"><h3>Wildlife-safe</h3><p>Raptor-safe rodenticides only.</p></article>
      </div>
    </div>
  </div>
</section>

<!-- ===================== ZONAS ===================== -->
<section class="band band--2 pad">
  <div class="shell">
{head_block("Service areas", "Serving the greater Phoenix Valley",
  "Maricopa and Pinal County, with active service routes across the East Valley, West Valley, "
  "North Valley, and South Valley.")}
{areas(CITIES)}
  </div>
</section>

<!-- ===================== FAQ ===================== -->
<section class="band pad faq-host">
  <div class="shell">
{head_block("FAQ", "Frequently asked questions",
  "Everything Phoenix Valley homeowners ask about general pest control.")}
{faq([
 ("How is Exclusive Pest Solutions different from other pest control companies in Phoenix?",
  "The core difference is our approach. Most pest control companies apply a standard spray on a "
  "fixed schedule regardless of what's actually happening at your property. We begin with a full "
  "evaluation, identify the specific pests and conditions present, and build a treatment plan "
  "around your home, not a templated route schedule."),
 ("How often do I need pest control service in the Phoenix Valley?",
  "Pest pressure in Arizona is year-round, though it shifts by season. Scorpion activity peaks in "
  "warmer months, cricket and mosquito populations spike during and after monsoon, and ant "
  "activity increases in spring. We'll recommend a service frequency based on your property's "
  "specific needs and pest history."),
 ("Are your treatments safe for my children and pets?",
  "Yes. Family and pet safety is a primary consideration in every product selection we make. "
  "We'll always provide pre- and post-treatment instructions and are happy to answer any "
  "questions about the products we use before we begin."),
 ("Do you offer one-time treatments or only ongoing service?",
  "We offer both. Some pest problems, a single bee hive or a one-time cricket surge, are addressed "
  "effectively with a single treatment. Others, like scorpion or ant infestations, benefit from an "
  "ongoing management plan. We'll give you an honest recommendation based on your situation."),
 ("What if I see pests after treatment?",
  "Some post-treatment activity is normal as pests emerge from harborage areas and contact treated "
  "surfaces. If you're seeing activity beyond what we'd expect, contact us. We stand behind our "
  "work and will return to assess and address the issue."),
 ("Do you serve the entire Phoenix Valley?",
  "Yes, we serve all of Maricopa County and Pinal County, including Phoenix, Scottsdale, Mesa, "
  "Gilbert, Chandler, Tempe, Glendale, Peoria, Surprise, Queen Creek, Fountain Hills, Cave Creek, "
  "Goodyear, Buckeye, Maricopa, and Casa Grande."),
])}
  </div>
  <img class="faq-owl" src="build-assets/owl-mark.png" alt="" width="448" height="425" loading="lazy" aria-hidden="true">
  <picture class="cactus faq-cactus">
    <source srcset="build-assets/cactus-mark2.webp" type="image/webp">
    <img src="build-assets/cactus-mark2.png" alt="" width="520" height="737" loading="lazy" aria-hidden="true">
  </picture>
</section>
'''
+ C.cta("One plan. Every pest. Done right.",
        "Every evaluation is on-site, no obligation, and tailored to the pest profile of your "
        "specific property. Maricopa and Pinal County.")
)

print(page("general-pest-control.html",
  "General Pest Control Phoenix AZ | One Plan for Every Pest",
  "One custom pest control plan for every Phoenix Valley pest: scorpions, ants, spiders, roaches, "
  "crickets and more. IPM based, garden-safe and family-safe. Licensed in Arizona.",
  [("Home","index.html"),("Services","index.html#services"),("General Pest Control",None)],
  body, "general"))
