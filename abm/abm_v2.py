# %%
import random
from mesa import Agent, Model
from mesa.datacollection import DataCollector

TICK_RATE = 0.1

KNOCKBACK_DISTANCES = {
    "none": 0,
    "light": 2.5,
    "medium": 10.0,
    "heavy": 50.0,
    "reverse": -15
}

DASH_CONFIG = {
    "stamina_cost": 5,
    "cooldown": 8,
    "invuln_duration": 0,
    "distance": 50,
}

CRUSADER_STATS = {
    "Redd":  {"max_health": 300, "max_stamina": 150, "walk_speed": 16, "run_speed": 24},
    "Yello": {"max_health": 250, "max_stamina": 175, "walk_speed": 15.5, "run_speed": 25},
    "Gleen": {"max_health": 325, "max_stamina": 100, "walk_speed": 17, "run_speed": 22},
    "Bluee": {"max_health": 275, "max_stamina": 125, "walk_speed": 16.5, "run_speed": 23},
}

WEAPON_MOVES = {
    "Redd": {
        "feint": {
            "damage": 20, "range": 5, "cooldown": 14, "stamina_cost": 0,
            "startup": 0.3, "active_duration": 0.3, "endlag": 0, "hitstun": 1.25,
            "tag": "combo_starter", "atk_type": "light", "tracking": True
        },
        "supernova": {
            "base_shockwave_damage": 20, "shockwave_range": 30,
            "base_slash_damage": 55, "slash_range": 8, "slash_delay": 0.125,
            "cooldown": 23, "stamina_cost": 0,
            "startup": 0.5, "active_duration": 0.375, "endlag": 0.875, "hitstun": 1.5,
            "tag": "punish", "atk_type": "heavy", "tracking": False
        },
        "blade_parade": { 
            "base_damage": 5, "range": 10, "dot_interval": 0.1,
            "self_damage_ratio": 1 / 8,
            "cooldown": 20, "stamina_cost": 0,
            "startup": 0.25, "active_duration": 1, "endlag": 0.5, "hitstun": 0.1,
            "tag": "poke", "atk_type": None, "tracking": True
        },
        "chanticleer_counter": { 
            "reflect_stat": 8, "buff_duration": 2.0,
            "cooldown": 30, "stamina_cost": 0,
            "startup": 0.1, "active_duration": 2, "endlag": 0.0, "hitstun": 0.0,
            "self_effect": "reflect", "tag": "defensive", "tracking": True
        },
    },
    "Yello": {
        "lasso": { 
            "damage": 20, "range": 25, "cooldown": 13, "stamina_cost": 0,
            "startup": 0.3, "active_duration": 0.35, "endlag": 0.25, "hitstun": 0.9,
            "borean_blitz_stamina_gain": 15,
            "tag": "combo_starter", "atk_type": "light", "tracking": True
        },
        "lighthouse": { 
            "damage": 0, "range": 4.5,
            "borean_blitz_damage": 10, "borean_blitz_range": 5.0, "borean_blitz_stamina_gain": 30,
            "cooldown": 12, "stamina_cost": 0,
            "startup": 0.4, "active_duration": 0.2, "endlag": 0, "hitstun": 1.25,
            "disables_attacks": True,
            "tag": "poke", "atk_type": "light", "tracking": True
        },
        "breakaway": { 
            "damage": 30, "range": 42.5, "cooldown": 17, "stamina_cost": 0,
            "startup": 0.35, "active_duration": 0.55, "endlag": 0, "hitstun": 0.5,
            "borean_blitz_stamina_gain": 15,
            "tag": "punish", "atk_type": "medium", "tracking": False
        },
        "borean_blitz": {
            "buff_duration": 5.0, "cooldown": 23, "stamina_cost": 0,
            "startup": 0.2, "active_duration": 0.0, "endlag": 0.0, "hitstun": 0.0,
            "self_effect": "borean_blitz", "tag": "defensive", "tracking": True
        },
    },
    "Gleen": {
        "yeet": { 
            "damage": 25, "target_distance": 35, "hitbox_radius": 5, 
            "cooldown": 20, "stamina_cost": 0,
            "startup": 0.4, "active_duration": 0.4, "endlag": 0.2, "hitstun": 0.5,
            "tag": "poke", "atk_type": "medium", "tracking": False
        },
        "accretion_disk": { 
            "damage": 25, "drain_stamina": 10, "range": 10, "cooldown": 23, "stamina_cost": 0,
            "startup": 0.3, "active_duration": 4.0, "endlag": 0, "hitstun": 0,
            "disables_attacks": False,
            "tag": "combo_starter", "atk_type": "heavy", "tracking": True
        },
        "anchor_point": {
            "shield_stat": 35, "buff_duration": 8.0, "speed_divisor": 2,
            "cooldown": 26, "stamina_cost": 0,
            "startup": 0.25, "active_duration": 0.0, "endlag": 0.0, "hitstun": 0,
            "disables_attacks": True,
            "self_effect": "shield", "tag": "defensive", "tracking": True
        },
        "ghillie_groundbreaker": {
            "damage": 50, "range": 8, "cooldown": 30, "stamina_cost": 10,
            "startup": 1.9, "travel_distance": 39.0, "active_duration": 0.5, "endlag": 0.5, "hitstun": 1.35,
            "bypass_invuln": True,
            "tag": "punish", "atk_type": "heavy", "tracking": True
        },
    },
    "Bluee": {
        "rend": {
            "damage": 75, "range": 6, "cooldown": 15, "stamina_cost": 0,
            "startup": 1.0, "dash_delay": 0.3, "dash_duration": 0.7, "dash_distance": 30.0,
            "active_duration": 0.1, "endlag": 0.3, "hitstun": 1.35,
            "bypass_invuln": True,
            "whiff_self_damage_ratio": 0.1, "whiff_self_stun": 0.5,
            "tag": "punish", "atk_type": "heavy", "tracking": True
        },
        "oumuamua": { 
            "cooldown": 20, "stamina_cost": 0,
            "startup": 0.15, "active_duration": 0.15, "endlag": 0.0, "hitstun": 0.15,
            "self_effect": "cooldown_refund",
            "tag": "defensive", "atk_type": "light", "tracking": True
        },
        "sword_trick": { 
            "dot_damage": 15, "dot_duration": 0.8, "finisher_damage": 20,
            "range": 8, "cooldown": 20, "stamina_cost": 0,
            "startup": 0.25, "active_duration": 1.0, "endlag": 0.25, "hitstun": 0.15,
            "self_speed_divisor": 3, "disables_attacks": True,
            "tag": "combo_starter", "atk_type": "light", "tracking": True
        },
        "protean_pace": { 
            "solid_damage": 50, "solid_range": 5,
            "liquid_damage": 5, "liquid_range": 10, "liquid_followup_damage": 35, "liquid_followup_delay": 0.5,
            "gas_damage": 25, "gas_range": 10,
            "cooldown": 18, "stamina_cost": 0,
            "startup": 0.35, "active_duration": 0.25, "endlag": 0, "hitstun": 0.9,
            "self_effect": "stance_check", "tag": "poke", "atk_type": "heavy", "tracking": False
        },
    },
}

WEAPON_M1_CONFIG = {
    "Redd":  {"base_dmg": 5,    "weapon_dmg_bonus": 1.25, "range": 3.5 + 2.5, "stamina_cost": 5,
              "combo_extension": 0.9,  "startup_delays": [0.2, 0.2, 0.2, 0.2],
              "active_durations": [0.1, 0.1, 0.1, 0.15],
              "cooldowns": [0.399, 0.399, 0.399, 2.249], "hitstun_times": [0.6, 0.6, 0.6, 0]},
    "Yello": {"base_dmg": 4.85, "weapon_dmg_bonus": 0.85, "range": 3.5 + 3.5, "stamina_cost": 5,
              "combo_extension": 0.8,  "startup_delays": [0.15, 0.15, 0.15, 0.3],
              "active_durations": [0.1, 0.1, 0.1, 0.15],
              "cooldowns": [0.299, 0.299, 0.299, 1.999], "hitstun_times": [0.35, 0.35, 0.35, 0.1]},
    "Gleen": {"base_dmg": 4.95, "weapon_dmg_bonus": 0.95, "range": 3.5 + 2.75, "stamina_cost": 5,
              "combo_extension": 1.0,  "startup_delays": [0.25, 0.25, 0.25, 0.25],
              "active_durations": [0.1, 0.1, 0.1, 0.2],
              "cooldowns": [0.499, 0.499, 0.499, 2.499], "hitstun_times": [0.55, 0.55, 0.55, 0]},
    "Bluee": {"base_dmg": 5,    "weapon_dmg_bonus": 1, "range": 3.5 + 2.5,  "stamina_cost": 5,
              "combo_extension": 0.9,  "startup_delays": [0.2, 0.2, 0.2, 0.2],
              "active_durations": [0.1, 0.1, 0.1, 0.15],
              "cooldowns": [0.399, 0.399, 0.399, 2.249], "hitstun_times": [0.55, 0.55, 0.55, 0]},
}


class Crusader(Agent):
    TAG_PRIORITY = {
        "poke": lambda self, target: True,
        "punish": lambda self, target: self.opponent_is_winding_up() or self.model.distance <= 40,
        "combo_starter": lambda self, target: target.stunned_until <= self.model.steps,
        "defensive": lambda self, target: self.opponent_is_winding_up() or self.health < self.max_health * 0.3,
    }

    def __init__(self, model, crusader_name):
        super().__init__(model)
        stats = CRUSADER_STATS[crusader_name]
        self.crusader_name = crusader_name
        self.health = stats["max_health"]
        self.max_health = stats["max_health"]
        self.stamina = stats["max_stamina"]
        self.max_stamina = stats["max_stamina"]
        self.walk_speed = stats["walk_speed"]
        self.run_speed = stats["run_speed"]
        self.stunned_until = 0
        self.locked_until = 0
        self.attacks_disabled_until = 0 
        self.invulnerable_until = 0
        self.resistant_until = 0
        self.dash_cooldown_until = 0
        self.sanity_lost = 0.0

        self.pending_move = None
        self.active_move = None
        self.active_until = 0
        self.has_hit_target = False  # prevents multiple hits during active damage frames

        self.pending_resolve_at = 0
        self.delayed_hits = [] 

        self.move_stats = {}  # move_name -> {"hits": int, "damage": float}
        self.rl_action_taken = False  # set by an external controller (e.g. SelfPlayMesaEnv) this tick

        self.dot_tick_last = 0
        self.dot_self_damage_applied = False

        self.reflect_divisor = None
        self.reflect_until = 0
        self.borean_blitz_until = 0
        self.shield_health = None
        self.shield_until = 0

        self.moves = WEAPON_MOVES[crusader_name]
        self.cooldowns = {name: 0 for name in self.moves}
        self.cooldowns["_m1_cd"] = 0

        self.m1_config = WEAPON_M1_CONFIG[crusader_name]
        self.m1_count = 0
        self.m1_last_use = -9999

    @property
    def health_lost(self):
        return self.max_health - self.health

    def alive(self):
        return self.health > 0

    def is_busy(self):
        return self.model.steps < self.stunned_until or self.model.steps < self.locked_until

    def attacks_disabled(self):
        return self.model.steps < self.attacks_disabled_until

    def has_borean_blitz(self):
        return self.model.steps < self.borean_blitz_until

    def opponent(self):
        others = [a for a in self.model.agents if a is not self]
        return others[0] if others else None

    def _record_move_stat(self, damage):
        move_name = self.active_move or self.pending_move or "unknown"
        stat = self.move_stats.setdefault(move_name, {"hits": 0, "damage": 0.0})
        stat["hits"] += 1
        stat["damage"] += damage

    def opponent_is_winding_up(self):
        target = self.opponent()
        return target is not None and target.pending_move is not None

    def opponent_is_invulnerable(self):
        target = self.opponent()
        return target is not None and target.invulnerable_until > self.model.steps

    def can_dash(self):
        return (
            self.model.steps >= self.dash_cooldown_until
            and self.stamina >= DASH_CONFIG["stamina_cost"]
            and not self.is_busy()
        )

    def perform_dash(self):
        self.stamina -= DASH_CONFIG["stamina_cost"]
        cd_ticks = int(DASH_CONFIG["cooldown"] / TICK_RATE)
        invuln_ticks = int(DASH_CONFIG["invuln_duration"] / TICK_RATE)
        self.dash_cooldown_until = self.model.steps + cd_ticks
        self.invulnerable_until = self.model.steps + invuln_ticks
        self.model.distance += DASH_CONFIG["distance"]
        self.pending_move = None
        self.active_move = None

    def apply_hit(self, damage, hitstun_sec=0.0, knockback_type=None, ignore_invuln=False, attacker=None):
        if not ignore_invuln and self.model.steps < self.invulnerable_until:
            return False

        if self.reflect_divisor and self.model.steps < self.reflect_until and attacker is not None:
            attacker.health -= damage / self.reflect_divisor
            return True

        if self.shield_health is not None and self.model.steps < self.shield_until:
            self.shield_health -= damage
            if self.shield_health < 0:
                overflow = -self.shield_health
                remaining_ticks = self.shield_until - self.model.steps
                self.locked_until = max(self.locked_until, self.model.steps + remaining_ticks)
                self.attacks_disabled_until = max(self.attacks_disabled_until, self.model.steps + remaining_ticks)
                self.shield_health = None
                self.walk_speed = CRUSADER_STATS[self.crusader_name]["walk_speed"]
                damage = overflow
            else:
                return True 

        if attacker is not None:
            attacker._record_move_stat(damage)

        self.health -= damage

        resistant = self.model.steps < self.resistant_until
        if not resistant:
            if self.pending_move or self.active_move:
                self.pending_move = None
                self.active_move = None
                self.locked_until = self.model.steps

            self.m1_count = 0

            if hitstun_sec > 0:
                hitstun_ticks = int(hitstun_sec / TICK_RATE)
                self.stunned_until = max(self.stunned_until, self.model.steps + hitstun_ticks)

            if knockback_type and knockback_type in KNOCKBACK_DISTANCES:
                self.model.distance = max(0.0, self.model.distance + KNOCKBACK_DISTANCES[knockback_type])

        return True

    def get_dynamic_move_specs(self, move_name):
        base_move = None
        for moves in WEAPON_MOVES.values():
            if move_name in moves:
                base_move = moves[move_name].copy()
                break

        if base_move is None:
            raise KeyError(f"Move '{move_name}' not found in WEAPON_MOVES dictionary.")

        if self.crusader_name == "Redd":
            loss_ratio = self.health_lost / self.max_health
            if move_name == "supernova":
                mult = 1.0 + (loss_ratio ** 2)
                base_move["base_shockwave_damage"] *= mult
                base_move["base_slash_damage"] *= mult
                self.sanity_lost += 0.05
            elif move_name == "blade_parade":
                base_move["base_damage"] *= (1.0 + (loss_ratio ** 2))
                self.sanity_lost += 0.05
            elif move_name == "chanticleer_counter":
                a = self.max_health + 50
                b = (base_move["reflect_stat"] ** 0.5) / a
                base_move["reflect_stat"] = -(b * self.health_lost) ** 2 + base_move["reflect_stat"]
                self.sanity_lost += 0.05

        elif self.crusader_name == "Gleen" and move_name == "anchor_point":
            a = self.max_health
            b = (base_move["shield_stat"] ** (1 / 3)) / a
            base_move["shield_stat"] = -(b * (self.health_lost - a)) ** 3 + 75
            self.sanity_lost += 0.05

        return base_move

    def m1_next_stage(self):
        ext = int(self.m1_config["combo_extension"] / TICK_RATE)
        if self.model.steps - self.m1_last_use <= ext:
            return min(4, self.m1_count + 1)
        return 1

    def m1_stage_damage(self, stage):
        base = self.m1_config["base_dmg"] + 0.5 * (stage - 1) ** 2
        return base + self.m1_config["weapon_dmg_bonus"]

    def use_m1(self):
        stage = self.m1_next_stage()
        self.m1_count = stage
        self.m1_last_use = self.model.steps
        self.stamina -= self.m1_config["stamina_cost"]

        startup_sec = self.m1_config["startup_delays"][stage - 1]
        active_sec = self.m1_config["active_durations"][stage - 1]
        
        startup_ticks = max(1, int(startup_sec / TICK_RATE))
        active_ticks = max(1, int(active_sec / TICK_RATE))
        stage_cd_sec = self.m1_config["cooldowns"][stage - 1]
        
        total_lock_ticks = startup_ticks + active_ticks + int(0.05 / TICK_RATE)
        self.cooldowns["_m1_cd"] = total_lock_ticks + int(stage_cd_sec / TICK_RATE)

        self.locked_until = self.model.steps + total_lock_ticks
        self.pending_move = f"m1_stage_{stage}"
        self.pending_resolve_at = self.model.steps + startup_ticks

    def start_move(self, move_name):
        move = self.get_dynamic_move_specs(move_name)
        self.stamina -= move.get("stamina_cost", 0)
    
        startup_ticks = int(move.get("startup", 0) / TICK_RATE)
        active_ticks = int(move.get("active_duration", 0) / TICK_RATE)
        endlag_ticks = int(move.get("endlag", 0) / TICK_RATE)
    
        total_lock_ticks = startup_ticks + active_ticks + endlag_ticks
        self.cooldowns[move_name] = total_lock_ticks + int(move["cooldown"] / TICK_RATE)

        if move.get("disables_attacks"):
            self.attacks_disabled_until = max(self.attacks_disabled_until, self.model.steps + total_lock_ticks)

        # specific moves allow movement
        if move_name == "sword_trick" or move_name == "lighthouse" or move_name == "accretion_disk":
            self.locked_until = self.model.steps
        else:
            self.locked_until = self.model.steps + total_lock_ticks

        self.pending_move = move_name
        self.pending_resolve_at = self.model.steps + startup_ticks

    def enter_active_frames(self, move_name):
        self.pending_move = None
        self.active_move = move_name
        self.has_hit_target = False
        self.dot_tick_last = self.model.steps - 999999  # let the first tick fire immediately
        self.dot_self_damage_applied = False

        if move_name.startswith("m1_stage_"):
            stage = int(move_name.split("_")[-1])
            active_sec = self.m1_config["active_durations"][stage - 1]
        else:
            move = self.get_dynamic_move_specs(move_name)
            active_sec = move.get("active_duration", 0)

            # advance 50 units (studs) upon entering active frames for ghillie groundbreaker
            if move_name == "ghillie_groundbreaker":
                travel_dist = move.get("travel_distance", 50.0)
                self.model.distance = max(0.0, self.model.distance - travel_dist)

            # rend is a dash-punish: close the dash gap before the hit check happens,
            # same pattern as ghillie_groundbreaker above!!! without this it never moves
            # and its real threat range silently collapses to the 6-stud melee range.
            if move_name == "rend":
                dash_dist = move.get("dash_distance", 30.0)
                self.model.distance = max(0.0, self.model.distance - dash_dist)

        active_ticks = max(1, int(active_sec / TICK_RATE))
        self.active_until = self.model.steps + active_ticks

    def process_active_frames(self):
        if not self.active_move:
            return
        # blade_parade ticks repeatedly across its whole active window, so it must not
        # be shut out by the single-hit gate the way every other move is.
        if self.has_hit_target and self.active_move != "blade_parade":
            return

        target = self.opponent()
        if not target or not target.alive():
            return

        current_distance = self.model.distance

        if self.active_move.startswith("m1_stage_"):
            stage = int(self.active_move.split("_")[-1])
            if current_distance <= self.m1_config["range"]:
                damage = self.m1_stage_damage(stage)
                hitstun_sec = self.m1_config["hitstun_times"][stage - 1]
                hit_success = target.apply_hit(damage=damage, hitstun_sec=hitstun_sec,
                                               knockback_type="light", attacker=self)
                if hit_success:
                    self.has_hit_target = True
                    if stage >= 4:
                        self.m1_count = 0
                    if self.has_borean_blitz():
                        self.stamina = min(self.max_stamina, self.stamina + 6)
            return

        move_name = self.active_move
        move = self.get_dynamic_move_specs(move_name)

        # Handle active damage frames for special moves
        if move_name == "feint" and current_distance <= move["range"]:
            target.apply_hit(damage=move["damage"], hitstun_sec=move["hitstun"],
                             knockback_type=move.get("atk_type"), attacker=self)
            self.has_hit_target = True

        elif move_name == "supernova":
            if current_distance <= move["shockwave_range"]:
                target.apply_hit(damage=move["base_shockwave_damage"], attacker=self)
            if current_distance <= move["slash_range"]:
                self.delayed_hits.append({
                    "resolve_tick": self.model.steps + max(1, int(move["slash_delay"] / TICK_RATE)),
                    "damage": move["base_slash_damage"], "hitstun": move["hitstun"],
                    "knockback_type": "heavy", "ignore_invuln": False,
                })
            self.has_hit_target = True

        elif move_name == "blade_parade" and current_distance <= move["range"]:
            interval_ticks = max(1, int(move.get("dot_interval", 0.1) / TICK_RATE))
            if self.model.steps - self.dot_tick_last >= interval_ticks:
                self.dot_tick_last = self.model.steps
                target.apply_hit(damage=move["base_damage"], hitstun_sec=move["hitstun"], attacker=self)
                if not self.dot_self_damage_applied:
                    self.health -= max(1, self.health * move["self_damage_ratio"])
                    self.dot_self_damage_applied = True
                self.has_hit_target = True  # marks "landed at least once" for stats/logic elsewhere;
                                             # process_active_frames' own gate ignores this for blade_parade

        elif move_name == "chanticleer_counter":
            self.reflect_divisor = move["reflect_stat"]
            self.reflect_until = self.model.steps + int(move["buff_duration"] / TICK_RATE)
            self.has_hit_target = True

        elif move_name == "lasso" and current_distance <= move["range"]:
            hit_success = target.apply_hit(damage=move["damage"], hitstun_sec=move["hitstun"], attacker=self)
            self.model.distance = 3.0
            if hit_success and self.has_borean_blitz():
                self.stamina = min(self.max_stamina, self.stamina + move["borean_blitz_stamina_gain"])
            self.has_hit_target = True

        elif move_name == "lighthouse":
            borean_blitz = self.has_borean_blitz()
            dmg = move["borean_blitz_damage"] if borean_blitz else move["damage"]
            rng = move["borean_blitz_range"] if borean_blitz else move["range"]
            if current_distance <= rng:
                hit_success = target.apply_hit(damage=dmg, hitstun_sec=move["hitstun"], attacker=self) if dmg > 0 else False
                if hit_success and borean_blitz:
                    self.stamina = min(self.max_stamina, self.stamina + move["borean_blitz_stamina_gain"])
            self.has_hit_target = True

        elif move_name == "breakaway" and current_distance <= move["range"]:
            hit_success = target.apply_hit(damage=move["damage"], hitstun_sec=move["hitstun"],
                                           knockback_type=move.get("atk_type"), attacker=self)
            if hit_success and self.has_borean_blitz():
                self.stamina = min(self.max_stamina, self.stamina + move["borean_blitz_stamina_gain"])
            self.has_hit_target = True

        elif move_name == "borean_blitz":
            self.borean_blitz_until = self.model.steps + int(move["buff_duration"] / TICK_RATE)
            self.has_hit_target = True

        elif move_name == "yeet":
            if abs(current_distance - move["target_distance"]) <= move["hitbox_radius"]:
                target.apply_hit(damage=move["damage"], hitstun_sec=move["hitstun"],
                                 knockback_type=move.get("atk_type"), attacker=self)
                self.has_hit_target = True

        elif move_name == "accretion_disk" and current_distance <= move["range"]:
            target.apply_hit(damage=move["damage"], knockback_type=move.get("atk_type"), attacker=self)
            target.stamina = max(0, target.stamina - move["drain_stamina"])
            self.has_hit_target = True

        elif move_name == "anchor_point":
            self.shield_health = move["shield_stat"]
            self.shield_until = self.model.steps + int(move["buff_duration"] / TICK_RATE)
            self.walk_speed = CRUSADER_STATS[self.crusader_name]["walk_speed"] / move["speed_divisor"]
            self.has_hit_target = True

        elif move_name == "ghillie_groundbreaker" and current_distance <= move["range"]:
            target.apply_hit(damage=move["damage"], hitstun_sec=move["hitstun"],
                             knockback_type=move.get("atk_type"), ignore_invuln=move.get("bypass_invuln", False),
                             attacker=self)
            self.has_hit_target = True

        elif move_name == "rend":
            if current_distance <= move["range"]:
                target.apply_hit(
                    damage = move["damage"], 
                    hitstun_sec = move["hitstun"],
                    knockback_type = move.get("atk_type"), 
                    ignore_invuln = move.get("bypass_invuln", False),
                    attacker = self
                )
            else:
                # penalty: self-damage + 0.5s additional stun/endlag
                self.health -= max(1, self.max_health * move["whiff_self_damage_ratio"])
                extra_stun_ticks = int(move["whiff_self_stun"] / TICK_RATE)
                self.stunned_until = max(self.stunned_until, self.model.steps + extra_stun_ticks)
            self.has_hit_target = True

        elif move_name == "oumuamua":
            candidates = [n for n in self.moves if n != "oumuamua" and self.cooldowns[n] > 0]
            if candidates:
                refunded = random.choice(candidates)
                refund_ticks = int(self.moves[refunded]["cooldown"] / TICK_RATE)
                self.cooldowns[refunded] = max(0, self.cooldowns[refunded] - refund_ticks)
            self.has_hit_target = True

        elif move_name == "sword_trick" and current_distance <= move["range"]:
            target.apply_hit(
                damage=move["dot_damage"], 
                hitstun_sec=move["hitstun"],
                knockback_type=move.get("atk_type"), 
                attacker=self
            )
            self.delayed_hits.append({
                "resolve_tick": self.model.steps + max(1, int(move["dot_duration"] / TICK_RATE)),
                "damage": move["finisher_damage"], 
                "hitstun": move["hitstun"],
                "knockback_type": "medium", 
                "ignore_invuln": False,
            })
    
            # slow walk speed by factor of 3 for the remaining move duration
            slow_ticks = int((move["active_duration"] + move["endlag"]) / TICK_RATE)
            self.slowed_until = self.model.steps + slow_ticks
            self.walk_speed = CRUSADER_STATS[self.crusader_name]["walk_speed"] / move["self_speed_divisor"]
            self.has_hit_target = True

        elif move_name == "protean_pace":
            hp_ratio = self.health / self.max_health
            if hp_ratio >= 2 / 3 and current_distance <= move["solid_range"]:
                target.apply_hit(damage=move["solid_damage"], hitstun_sec=move["hitstun"],
                                 knockback_type=move.get("atk_type"), attacker=self)
                self.has_hit_target = True
            elif hp_ratio > 1 / 3 and current_distance <= move["liquid_range"]:
                target.apply_hit(damage=move["liquid_damage"], attacker=self)
                self.delayed_hits.append({
                    "resolve_tick": self.model.steps + max(1, int(move["liquid_followup_delay"] / TICK_RATE)),
                    "damage": move["liquid_followup_damage"], "hitstun": move["hitstun"],
                    "knockback_type": "medium", "ignore_invuln": False,
                })
                self.has_hit_target = True
            elif current_distance <= move["gas_range"]:
                target.apply_hit(damage=move["gas_damage"], hitstun_sec=move["hitstun"],
                                 knockback_type="light", attacker=self)
                self.has_hit_target = True

    def choose_move(self):
        distance = self.model.distance
        target = self.opponent()

        if self.attacks_disabled():
            return None

        available = {}
        for name, data in self.moves.items():
            if self.cooldowns[name] > 0 or self.stamina < data.get("stamina_cost", 0):
                continue
            
            if name == "yeet":
                target_dist = data["target_distance"]
                radius = data["hitbox_radius"]
                if abs(distance - target_dist) <= radius:
                    available[name] = data
            elif name == "ghillie_groundbreaker":
                # Account for forward movement distance when checking range availability
                effective_range = data.get("range", 8) + data.get("travel_distance", 50.0)
                if distance <= effective_range:
                    available[name] = data
            elif name == "rend":
                # Same idea: Rend closes dash_distance before its hit check, so it needs
                # to be selectable from that far out, not just from melee range.
                effective_range = data.get("range", 6) + data.get("dash_distance", 30.0)
                if distance <= effective_range:
                    available[name] = data
            elif distance <= data.get("range", 999):
                available[name] = data

        if not available:
            return None

        priority_order = ["defensive", "punish", "combo_starter", "poke"]
        for tag_name in priority_order:
            condition_func = self.TAG_PRIORITY.get(tag_name)
            if condition_func and condition_func(self, target):
                matching_moves = [name for name, data in available.items() if data.get("tag") == tag_name]
                if matching_moves:
                    return random.choice(matching_moves)

        return random.choice(list(available.keys()))

    def step(self):
        if not self.alive():
            return

        skip_autonomous_action = self.rl_action_taken
        self.rl_action_taken = False

        for name in self.cooldowns:
            self.cooldowns[name] = max(0, self.cooldowns[name] - 1)

        self.stamina = min(self.max_stamina, self.stamina + 1)

        # process delayed hits
        for hit in self.delayed_hits[:]:
            if self.model.steps >= hit["resolve_tick"]:
                target = self.opponent()
                if target and target.alive():
                    target.apply_hit(damage=hit["damage"], hitstun_sec=hit["hitstun"],
                                     knockback_type=hit["knockback_type"],
                                     ignore_invuln=hit["ignore_invuln"], attacker=self)
                self.delayed_hits.remove(hit)

        # expire temporary effects
        if self.model.steps >= self.reflect_until:
            self.reflect_divisor = None
        if self.model.steps >= self.shield_until and self.shield_health is not None:
            self.shield_health = None
            self.walk_speed = CRUSADER_STATS[self.crusader_name]["walk_speed"]
            
        # reset walk speed after Sword Trick slow duration ends
        if hasattr(self, "slowed_until") and self.model.steps >= self.slowed_until and self.shield_health is None:
            self.walk_speed = CRUSADER_STATS[self.crusader_name]["walk_speed"]

        if self.model.steps < self.stunned_until:
            return

        # transition pending moves to active damage frames
        if self.pending_move and self.model.steps >= self.pending_resolve_at:
            self.enter_active_frames(self.pending_move)

        # evaluate active damage frame hits
        if self.active_move:
            if self.model.steps < self.active_until:
                self.process_active_frames()
            else:
                self.active_move = None  # damage frames expired

        if self.model.steps < self.locked_until:
            return

        if skip_autonomous_action:
            return

        # restore speed
        if not self.attacks_disabled() and self.walk_speed != CRUSADER_STATS[self.crusader_name]["walk_speed"] \
                and self.shield_health is None and getattr(self, "slowed_until", 0) <= self.model.steps:
            self.walk_speed = CRUSADER_STATS[self.crusader_name]["walk_speed"]

        target = self.opponent()

        if target and target.active_move:
            if self.can_dash():
                self.perform_dash()
                return
            else:
                retreat_speed = self.walk_speed * TICK_RATE
                self.model.distance += retreat_speed
                return
        
        if target and target.pending_move and self.can_dash():
            incoming_move = target.moves.get(target.pending_move, {})
            incoming_range = incoming_move.get("range", 0) + incoming_move.get("dash_distance", 0)
            if incoming_move.get("atk_type") == "heavy" and self.model.distance <= incoming_range:
                self.perform_dash()
                return

        if self.opponent_is_invulnerable():
            approach_speed = self.walk_speed * TICK_RATE
            self.model.distance = max(0, self.model.distance - approach_speed)
            return

        special_move = self.choose_move()
        if special_move:
            self.start_move(special_move)
            return

        m1_ready = (
            not self.attacks_disabled()
            and self.cooldowns.get("_m1_cd", 0) <= 0
            and self.stamina >= self.m1_config["stamina_cost"]
            and self.model.distance <= self.m1_config["range"]
        )
        if m1_ready:
            self.use_m1()
            return

        if self.stamina > self.max_stamina / 2:
            approach_speed = self.run_speed * TICK_RATE
            self.stamina -= 1
        else:
            approach_speed = self.walk_speed * TICK_RATE
        self.model.distance = max(0, self.model.distance - approach_speed)


class DuelModel(Model):
    def __init__(self, crusader_a="Gleen", crusader_b="Redd", seed=None):
        super().__init__(seed=seed)
        self.distance = 10.0
        Crusader(self, crusader_a)
        Crusader(self, crusader_b)
        self.datacollector = DataCollector(agent_reporters={"Health": "health", "Stamina": "stamina"})

    def fight_over(self):
        return any(not a.alive() for a in self.agents)

    def step(self):
        self.datacollector.collect(self)
        self.agents.shuffle_do("step")


if __name__ == "__main__":
    NUM_FIGHTS = 5000
    MAX_TICKS = 2000
    total_sanity_lost = 0.0

    MATCHUPS = [
        ("Redd", "Yello"), ("Redd", "Gleen"), ("Redd", "Bluee"),
        ("Yello", "Gleen"), ("Yello", "Bluee"), ("Gleen", "Bluee"),
    ]

    for a, b in MATCHUPS:
        wins = {a: 0, b: 0, "draw": 0}
        total_ticks = 0
        move_stats = {a: {}, b: {}}  # crusader_name -> move_name -> {"hits", "damage"}

        for fight_num in range(NUM_FIGHTS):
            model = DuelModel(a, b)
            ticks = 0
            while not model.fight_over() and ticks < MAX_TICKS:
                model.step()
                ticks += 1
            total_ticks += ticks

            winner = None
            for agent in model.agents:
                total_sanity_lost += agent.sanity_lost
                if agent.alive():
                    winner = agent.crusader_name
                for move_name, stat in agent.move_stats.items():
                    dest = move_stats[agent.crusader_name].setdefault(move_name, {"hits": 0, "damage": 0.0})
                    dest["hits"] += stat["hits"]
                    dest["damage"] += stat["damage"]

            wins[winner if winner else "draw"] += 1

        print(f"--- {a} vs {b} ({NUM_FIGHTS} fights) ---")
        for name, count in wins.items():
            print(f"  {name}: {count} wins ({count / NUM_FIGHTS:.1%})")
        print(f"  Average fight length: {total_ticks / NUM_FIGHTS:.1f} ticks")

        print(f"  --- move stats ---")
        for crusader_name in (a, b):
            print(f"  {crusader_name}:")
            sorted_moves = sorted(move_stats[crusader_name].items(), key=lambda kv: -kv[1]["damage"])
            for move_name, stat in sorted_moves:
                avg = stat["damage"] / stat["hits"] if stat["hits"] else 0
                print(f"    {move_name}: {stat['hits']} hits, {stat['damage']:.0f} total dmg (avg {avg:.1f}/hit)")
        print()

    print(f"Estimated Developer Sanity Lost: {total_sanity_lost:.1f} points")

# %%



