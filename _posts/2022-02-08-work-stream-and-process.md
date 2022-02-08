---
layout: default
title: Work Stream and Process
---

# Work Stream and Process

As we are working towards delivering on outcomes, we should recognize the reality that there will be other work that comes our way that is outside of the scope of our outcomes.  

This work can be in the form of support work, maintenance/paying down tech debt, unplanned work to support other teams, or new work that arises out of emerging or changing business priorities.  It's a good idea to plan the way we process around these realities so we don't get caught in a position where we can't support the business.

### <a name="product-and-engineering-reward-functions">Product and Engineering Reward Functions</a>

One of the fundamental things to understand about the balance between Product and Engineering is that each discipline has a distinct reward function that can be used to communicate what success looks like.

For Product, a healthy reward function involves balancing the needs of the Sales and Marketing departments with the inbound customer requests and long-term strategic investments that provide a market advantage for the business.  The outputs that are measured by this reward function are usually new features and capabilities of the system(s) the Product organization is supporting.  In a mature Product organization metrics such as customer-reported bugs, performance, and reliability are part of the reward function algorithm. 

For Engineering, the reward function is more complex.  The most heavily weighted component of an engineering reward function should be delivering the outputs that the Product organization needs in order to maximize their reward function.  In addition to Product deliverables, a healthy engineering reward function also weights things like system performance, code base health, extensibility, maintainability, low cognitive load, and ease of maintenance as heavily weighted components.  When the Product deliverables are weighted too heavily in the engineering reward function the Engineering organization is transformed into a "Feature Factory", and the health of the system suffers due to an imbalance of focus between the organizations.  If the Engineering side of the equation is weighted too heavily, there is a risk of failing to deliver on the Product outcomes that support the business.

Reward functions should be examined regularly to ensure that they are in balance, using metrics such as cycle time, technical debt, maintenance burden, and release dependencies as key indicators of system health.

---

### <a name="work-stream-design">Work Stream Design</a>

The process and discipline of work stream design is WAAAAY too big of a topic for a single post (much less a section of a post!), but it is important to think about work stream design when working with Engineering teams that will support Product organizations.  Some of the considerations to think about when designing a work stream are:

- How is work ingested to the team?
- How does a team determine if work that has been requested will be executed?
    -- What impact will the work have on our outcomes?  Would it require us to reexamine, and possibly abandon, our outcomes?
    -- Does Product communicate the strategic need for the work to the engineering team?
    -- Does the work fit the strategic direction of the product?
    -- If it does not, how can we help the Product organization understand where the work could be better incorporated?
- Once work has been accepted, how is it prioritized against work the team has already committed to?
- How is unplanned work handled?
- How is support work handled?  What is considered support work?
- Does the work stream make space for innovation and discovery?
    -- what constraints are placed on innovation and discovery activities to ensure they do not distract from the main work stream?

Discussing these questions on a regular basis is important to ensure that the work stream that is designed and refined supports our outcomes, as well as the the Product and Engineering organization reward functions in service of enabling delivery through maintaining a health system.

---

### <a name="process-design">Process Design</a>

Once we have designed the way in which work is introduced into and ingested by the team, that process should inform the process design for the team that enables work to be done, while enabling a healthy team culture.

The types of work that are being ingested by the team should be regularly discussed to determine if the amount of inbound work that is not directly related to outcomes is reasonable, or if it is in danger of impacting the teams ability to achieve their outcomes.

As discussed in **[Identifying and Communicating Risks](/2022/01/28/targets#identifying-and-communicating-risks)**, risks to achieving outcomes should be identified and communicated as soon as possible.

### <a name="investment-budgets">Investment Budgets</a>

One strategy for maintaining a healthy balance of work that supports outcomes and unplanned work that must be processed by the team is the concept of investment budgets.

Categorizing the types of work (Features/Outcome Work, Support, Maintenance/Tech Debt, Unplanned work) allows teams to track over time the amount of their time they are investing in a given category, and should allow the team to maintain healthy balances, so as to not overwhelm their ability to deliver on multiple fronts.

Investment budgets provide a deterministic, objective mechanism for the team to communicate to stakeholders how much of their time they can invest in a given category of work.  They can help provide prioritization and decision making points when pulling work in, and allow for strategic planning of future investments and commitments.

---

Thanks for reading about our framework for Outcome Based Software Delivery.  In my next post I'll write about a decision making framework for empowering teams, helping them understand the scope in which they can manuever freely, and understand when communication is necessary with other parts of the business to help make critical decisions.

Until then, have a great day!