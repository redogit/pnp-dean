# Charter — Dual Adversarial Proof Field

## Goal

Force progress on P versus NP by making the two theorem directions attack each other's exact obligations while sharing one immutable definitional substrate.

### Constructive direction

Produce one deterministic algorithm `A` for an NP-complete decision language and fixed constants `c,k` such that for every encoded input `x`:

[
A(x)=L(x)
]

and

[
T_A(|x|) \le c|x|^k+c.
]

### Lower-bound direction

Establish a theorem applying to every deterministic algorithm deciding the chosen NP-complete language such that no fixed polynomial bounds its worst-case work.

Defeating finitely many algorithms is not enough.

## Current common test domain

Dean / Independent Set:

Given finite conflict graph `G=(V,E)` and target `K`, decide whether an independent set of size at least `K` exists.

Original student identities and witnesses must remain reconstructible when a route claims witness preservation.

## Shared base

Both theorem directions use exactly the same:

- encoding;
- input length;
- deterministic cost model;
- language semantics;
- reduction rules;
- proof/admission rules.

The combatants may attack algorithms and representations. They may not redefine the game.

## Design hypothesis

Small populations can expose stronger invariants than one linear proof search if:

1. the constructive population is rewarded only for exact polynomial progress;
2. the adversarial population is rewarded only for genuine counterexamples or generalized obstructions;
3. a neutral referee prevents rhetorical wins;
4. diversity prevents collapse onto one carrier;
5. memory prevents rediscovery of dead routes;
6. cost accounting prevents hidden exponential work;
7. repeated local wins are distilled into lemmas rather than accumulated as anecdotes.

## Success

### P=NP success

One admitted universal construction discharging all required obligations.

### P!=NP success

One admitted universal lower-bound theorem. A cemetery of failed algorithms is not sufficient.

## Valuable fallback

Even without resolving P versus NP:

- enlarge exact polynomial terminal classes;
- prove new counterfamilies against proposed carriers;
- isolate representation-independent barriers;
- improve exact carrier/reconstruction theory;
- produce reusable, auditable negative results.

## Non-goals

- changing standard complexity definitions;
- treating neural confidence as proof;
- accepting an oracle hidden inside reconciliation;
- promoting bounded experiments to universal results;
- optimizing only wall-clock time while ignoring deterministic work;
- erasing failed approaches.
