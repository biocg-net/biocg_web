"""
Bio CG — Brushed Steel
NiceGUI + Tailwind implementation with mobile support.

Run:
    pip install nicegui
    python biocg_app.py

Then open http://localhost:8080
On your local network: http://<YOUR_IP>:8080
"""

from nicegui import ui


C = {
    "bg": "#f0eee9",
    "panel": "#ffffff",
    "surface": "#e8e5df",
    "ink": "#1a1c24",
    "ink_mid": "#3a3d4a",
    "muted": "#8a8d99",
    "rule": "#d4d0c8",
    "navy": "#1b2a4a",
    "navy_mid": "#2d4070",
    "gold": "#b8922a",
    "gold_lt": "#d4ab4a",
    "gold_line": "#c8a030",
    "gold_bg": "#faf5e8",
    "emerald": "#2a7a5a",
}

HEAD_HTML = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Mono:wght@300;400;500&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
.q-page  { padding: 0 !important; }
.nicegui-content { padding: 0 !important; max-width: 100% !important; }
</style>
"""


# ── DATA ─────────────────────────────────────────────────────────────────────

PILLARS = [
    {
        "tag": "IT",
        "title": "Bio Tech",
        "num": "#1",
        "accent": "#2d4070",
        "items": [
            ("sym_s_extension_off", "No AI led Design"),
            ("sym_s_code_off", "No full-AI Code"),
            ("sym_s_verified_off", "No full-AI Code Review"),
        ],
    },
    {
        "tag": "Management",
        "title": "Bio Prod",
        "num": "#2",
        "accent": "#c8a030",
        "items": [
            ("sym_s_receipt_long_off", "No AI Ref / Treatment"),
            ("sym_s_landscape_2_off", "No AI Concept Art"),
            ("sym_s_grid_off", "No AI Planning"),
        ],
    },
    {
        "tag": "Image",
        "title": "Bio Pixels",
        "num": "#3",
        "accent": "#2a7a5a",
        "items": [
            ("sym_s_attach_file_off", "no AI Source Material"),
            ("sym_s_edit_off", "no AI Editing"),
            ("sym_s_blur_off", "no AI Style/Render"),
        ],
    },
]

BADGE_CFG = {
    "pixel": ("Bio Pixel", "#2a7a5a", "rgba(42,122,90,0.08)"),
    "prod": ("Bio Prod", "#b8922a", "#faf5e8"),
    "tech": ("Bio Tech", "#2d4070", "rgba(27,42,74,0.08)"),
}

PILL_CFG = {
    "full": ("#2a7a5a", "#2a7a5a", "rgba(42,122,90,0.08)"),
    "mid": ("#b8922a", "#c8a030", "#faf5e8"),
    "low": ("#8a8d99", "#d4d0c8", "#e8e5df"),
}

STUDIOS = [
    {
        "name": "Ironframe Studio",
        "location": "Berlin, DE",
        "score": "9/9",
        "pill": "full",
        "badges": ["pixel", "prod", "tech"],
        "quote": "We believe every pixel should carry a fingerprint. Our work is signed with human intention.",
    },
    {
        "name": "Lightwell VFX",
        "location": "London, UK",
        "score": "6/9",
        "pill": "mid",
        "badges": ["pixel", "prod"],
        "quote": "Our artists are not prompt engineers. They're craftspeople, and that distinction matters.",
    },
    {
        "name": "Parallax Works",
        "location": "Montréal, CA",
        "score": "6/9",
        "pill": "mid",
        "badges": ["pixel", "tech"],
        "quote": "Human-authored visuals aren't a limitation — they're our competitive edge.",
    },
    {
        "name": "Grain & Light",
        "location": "Tokyo, JP",
        "score": "6/9",
        "pill": "mid",
        "badges": ["prod", "tech"],
        "quote": "The imperfection of human work is its soul. We won't trade that for convenience.",
    },
    {
        "name": "Render & Co.",
        "location": "New York, USA",
        "score": "3/9",
        "pill": "low",
        "badges": ["pixel"],
        "quote": "Clients come to us because they know a human made every creative choice.",
    },
]

FOOTER_LINKS = {
    "Navigate": ["About", "Members", "Resources", "Join"],
    "Community": ["Discord", "Linkedin", "GitHub", "Help us ❤︎"],
    "Legal": ["Licences", "Data Protection", "Partners"],
    # "Social": ["Twitter / X", "LinkedIn", "Instagram", "Mastodon"],
}

NAV_ITEMS = [
    "About",
    "Members",
    "Resources",
]

# ── HELPERS ──────────────────────────────────────────────────────────────────


def s(**kwargs) -> str:
    """Build an inline style string from keyword arguments.
    Underscores in key names are replaced with hyphens.
    """
    return "; ".join(f"{k.replace('_', '-')}:{v}" for k, v in kwargs.items())


def mono_label(
    text: str,
    size: str = "10px",
    color: str = None,
    spacing: str = "2px",
    upper: bool = True,
    extra: str = "",
) -> ui.label:
    color = color or C["muted"]
    transform = "uppercase" if upper else "none"
    return ui.label(text).style(
        s(
            font_family="DM Mono, monospace",
            font_size=size,
            letter_spacing=spacing,
            text_transform=transform,
            color=color,
        )
        + (f";{extra}" if extra else "")
    )


def bebas_label(
    text: str,
    size: str = "32px",
    color: str = None,
    spacing: str = "2px",
    extra: str = "",
) -> ui.label:
    color = color or C["ink"]
    return ui.label(text).style(
        s(
            font_family="Bebas Neue, sans-serif",
            font_size=size,
            letter_spacing=spacing,
            color=color,
            line_height="1.05",
        )
        + (f";{extra}" if extra else "")
    )


def pill_badge(key: str):
    label, color, bg = BADGE_CFG[key]
    ui.label(label).style(
        s(
            font_family="DM Mono, monospace",
            font_size="9px",
            letter_spacing="2px",
            text_transform="uppercase",
            padding="3px 9px",
            border=f"1px solid {color}",
            color=color,
            background=bg,
            white_space="nowrap",
            display="inline-block",
        )
    )


def gold_divider():
    ui.element("div").style(
        s(
            height="1px",
            background=f"linear-gradient(90deg,transparent,{C['gold_line']},transparent)",
            margin="20px 0",
        )
    )


# ── NAV ──────────────────────────────────────────────────────────────────────


def build_nav():
    with (
        ui.header(elevated=False)
        .style(
            s(
                background="rgba(240,238,233,0.96)",
                backdrop_filter="blur(5px)",
                border_bottom=f"1px solid {C['rule']}",
                # height="68px",
                # padding="0 48px",
            )
        )
        .classes("flex items-center xjustify-between gap-4")
    ):

        # Logo
        with ui.row().classes("items-center gap-3 cursor-pointer no-wrap"):
            logo = ui.image("/assets/favicon/favicon.svg").classes("w-[3em]")
            logo.on("click", logo.force_reload)
            bebas_label("Bio CG", size="22px", color=C["navy"], spacing="4px").classes(
                "text-nowrap"
            ).on("click", ui.navigate.reload)

        ui.space()

        # Desktop links — hidden below md breakpoint
        with ui.row().classes("items-center gap-6 max-md:hidden"):
            for item in NAV_ITEMS:
                ui.button(item, on_click=lambda: None).props("flat xno-caps").style(
                    s(
                        font_family="DM Mono, monospace",
                        # font_size="11px",
                        # letter_spacing="2px",
                        # text_transform="uppercase",
                        color=C["muted"],
                        # padding="0",
                        # min_height="unset",
                    )
                )

        ui.space()

        ui.button("Join", on_click=lambda: None).props("outline xno-caps").style(
            s(
                font_family="DM Mono, monospace",
                # font_size="11px",
                # letter_spacing="2px",
                # text_transform="uppercase",
                color=C["navy"],
                border=f"1px solid {C['navy']}",
                # padding="6px 20px",
                border_radius="0",
            )
        )

        # Mobile hamburger — visible below md
        with ui.element("div").classes("md:hidden"):
            with ui.button(icon="menu").props("flat round").style(s(color=C["navy"])):
                with (
                    ui.menu()
                    .props("auto-close")
                    .style(
                        s(
                            min_width="180px",
                            border_radius="0",
                            background=C["bg"],
                            border=f"1px solid {C['rule']}",
                        )
                    )
                ):
                    for item in NAV_ITEMS + ["Join"]:
                        ui.menu_item(item, on_click=lambda: None).style(
                            s(
                                font_family="DM Mono, monospace",
                                font_size="11px",
                                letter_spacing="2px",
                                text_transform="uppercase",
                                color=C["ink"],
                            )
                        )


# ── HERO ─────────────────────────────────────────────────────────────────────


def build_hero():
    # Outer wrapper — 3-col grid on desktop, 1-col stack on mobile
    with (
        ui.element("section")
        .classes("w-full grid grid-cols-1 md:grid-cols-[56px_2fr_1fr]")
        .style(
            s(
                min_height="86vh",
                border_bottom=f"1px solid {C['rule']}",
            )
        )
    ):

        # Film strip (hidden on mobile)
        with (
            ui.column()
            .classes("max-md:hidden items-center justify-around py-6")
            .style(
                s(
                    background=C["navy"],
                )
            )
        ):
            for _ in range(20):
                ui.element("div").style(
                    s(
                        width="20px",
                        height="20px",
                        border_radius="2px",
                        background=C["bg"],
                        opacity="0.25",
                    )
                )

        # Hero text panel
        with (
            ui.column()
            .classes("justify-center gap-0 p-8 md:px-16 md:py-20")
            .style(
                s(
                    background=C["panel"],
                    border_right=f"1px solid {C['rule']}",
                    border_bottom=f"1px solid {C['rule']}",
                )
            )
        ):

            # Eyebrow
            with ui.row().classes("items-center gap-4 mb-7 anim-r1"):
                ui.element("div").style(
                    s(
                        width="28px",
                        height="1px",
                        background=C["gold_line"],
                        flex_shrink="0",
                    )
                )
                mono_label(
                    "Promoting human craft in CG",
                    size="10px",
                    color=C["gold"],
                    spacing="4px",
                )

            # H1 — uses ui.html for the outline ghost effect which needs CSS text-stroke
            ui.html(
                f"""
                <h1 class="anim-r2" style="
                    font-family:'Bebas Neue',sans-serif;
                    font-size:clamp(60px,8.5vw,108px);
                    line-height:0.93; letter-spacing:1px;
                    color:{C['ink']}; margin-bottom:32px;">
                  <span style="color:{C['navy']}">Biological</span>
                  <br>Computer Graphics<br>
                  <span style="color:{C['navy']}">by</span>
                  <span style="-webkit-text-stroke:1.5px {C['rule']};color:transparent">Humans.</span><br>
                </h1>
            """
            )

            ui.label(
                "Bio CG is a movement of studios and artists committed to keeping "
                "human hands at the heart of computer graphics — from draft "
                "to final frame."
            ).classes("anim-r3 mb-12 max-w-md").style(
                s(
                    font_size="17px",
                    line_height="1.68",
                    color=C["ink_mid"],
                )
            )

            with ui.row().classes("gap-3 flex-wrap anim-r3"):
                ui.button("Engage Your Studio", on_click=lambda: None).props(
                    "no-caps"
                ).style(
                    s(
                        font_family="DM Mono, monospace",
                        font_size="11px",
                        letter_spacing="2px",
                        text_transform="uppercase",
                        background=C["navy"],
                        color=C["gold_lt"],
                        border_radius="0",
                        padding="14px 32px",
                    )
                )
                ui.button("Learn More", on_click=lambda: None).props(
                    "outline no-caps"
                ).style(
                    s(
                        font_family="DM Mono, monospace",
                        font_size="11px",
                        letter_spacing="2px",
                        text_transform="uppercase",
                        color=C["muted"],
                        border=f"1px solid {C['rule']}",
                        border_radius="0",
                        padding="14px 32px",
                    )
                )

        # VIP Navy sidebar
        with (
            ui.column()
            .classes("justify-end")
            .style(
                s(
                    background=C["navy"],
                    background_image=(
                        "repeating-linear-gradient(-45deg,"
                        "rgba(255,255,255,0.03) 0,rgba(255,255,255,0.03) 1px,"
                        "transparent 1px,transparent 12px)"
                    ),
                    position="relative",
                    overflow="hidden",
                )
            )
        ):
            with ui.column().classes("relative z-10 gap-0 p-10 md:p-12"):

                # Member card
                with ui.card().style(
                    s(
                        border="1px solid rgba(184,146,42,0.5)",
                        background="rgba(184,146,42,0.06)",
                        border_radius="0",
                        box_shadow="none",
                        position="relative",
                        margin_bottom="24px",
                    )
                ):
                    # Floating label
                    ui.label("Bio CG Member").style(
                        s(
                            font_family="DM Mono, monospace",
                            font_size="8px",
                            letter_spacing="4px",
                            text_transform="uppercase",
                            color=C["gold"],
                            position="absolute",
                            top="-1px",
                            left="20px",
                            background=C["navy"],
                            padding="0 8px",
                            transform="translateY(-50%)",
                        )
                    )
                    with ui.card_section():
                        bebas_label(
                            "Ironframe Studio",
                            size="26px",
                            color="#f0e8d0",
                            extra="margin-bottom:4px;display:block",
                        )
                        mono_label(
                            "Berlin, DE · Member since 2025",
                            size="10px",
                            color="rgba(184,146,42,0.7)",
                            spacing="1.5px",
                        )

                # Stats 2×2 grid
                with ui.grid(columns=2).style(
                    s(
                        gap="1px",
                        background="rgba(255,255,255,0.06)",
                        border="1px solid rgba(255,255,255,0.08)",
                    )
                ):
                    for val, lbl in [
                        ("24", "Studios"),
                        ("9/9", "Top Score"),
                        ("3", "Pillars"),
                        ("8", "Full Pledge"),
                    ]:
                        with (
                            ui.column()
                            .classes("gap-0")
                            .style(
                                s(
                                    background=C["navy"],
                                    padding="18px 22px",
                                )
                            )
                        ):
                            bebas_label(val, size="38px", color=C["gold_lt"])
                            mono_label(
                                lbl,
                                size="9px",
                                color="rgba(255,255,255,0.3)",
                                spacing="2px",
                            )

                gold_divider()

                mono_label(
                    "Bio CG — Human Made · Est. 2025",
                    size="9px",
                    color="rgba(255,255,255,0.25)",
                    spacing="2px",
                    extra="text-align:center;display:block",
                )


# ── SCORE SECTION ─────────────────────────────────────────────────────────────


def build_score_section():
    with (
        ui.element("section")
        .classes("w-full px-5 py-14 md:px-14 md:py-20 lg:pl-28")
        .style(
            s(
                background=C["bg"],
                border_bottom=f"1px solid {C['rule']}",
            )
        )
    ):
        # Section label
        with ui.row().classes("items-center gap-4 mb-12"):
            mono_label("The Bio CG Score", size="10px", color=C["gold"], spacing="4px")
            ui.element("div").style(
                s(
                    width="48px",
                    height="1px",
                    background=C["gold_line"],
                )
            )

        with ui.grid(columns=3).classes("gap-5 w-full grid-cols-1 md:grid-cols-3"):
            for p in PILLARS:
                with (
                    ui.card()
                    .style(
                        s(
                            background=C["panel"],
                            border=f"1px solid {C['rule']}",
                            border_top=f"3px solid {p['accent']}",
                            border_radius="0",
                            box_shadow="none",
                            position="relative",
                            overflow="hidden",
                            # transition="transform 0.25s, box-shadow 0.25s",
                        )
                    )
                    .classes("transition duration-250 hover:scale-105 hover:z-10")
                ):
                    with ui.card_section().classes("p-8 md:p-9"):
                        mono_label(
                            p["tag"],
                            size="10px",
                            color=p["accent"],
                            spacing="3px",
                            extra="display:block;margin-bottom:6px",
                        )
                        bebas_label(
                            p["title"],
                            size="30px",
                            extra="display:block;margin-bottom:24px",
                        )
                        with ui.column().classes("gap-3"):
                            for icon, item_text in p["items"]:
                                with ui.row().classes("items-center gap-2"):
                                    ui.label("—").style(
                                        s(
                                            font_size="10px",
                                            color=p["accent"],
                                            flex_shrink="0",
                                        )
                                    )
                                    ui.icon(icon, size="md", color=p["accent"])
                                    mono_label(
                                        item_text,
                                        size="12px",
                                        color=C["muted"],
                                        upper=False,
                                    )
                        # Ghost number
                    ui.label(p["num"]).style(
                        s(
                            font_family="Bebas Neue, sans-serif",
                            font_size="72px",
                            color=C["rule"],
                            line_height="1",
                            position="absolute",
                            bottom="16px",
                            right="20px",
                            opacity="0.5",
                            pointer_events="none",
                        )
                    )


# ── CALLOUT ──────────────────────────────────────────────────────────────────


def build_callout():
    with (
        ui.element("section")
        .classes("w-full")
        .style(
            s(
                background=C["navy"],
                border_bottom="1px solid #0f1a30",
                position="relative",
                # overflow="hidden",
                background_image=(
                    "repeating-linear-gradient(-45deg,"
                    "rgba(255,255,255,0.02) 0,rgba(255,255,255,0.02) 1px,"
                    "transparent 1px,transparent 14px)"
                ),
            )
        )
    ):
        with ui.row().classes(
            "w-full items-center flex-col md:flex-row gap-10 md:gap-20 "
            "px-5 py-14 md:px-14 md:py-24 lg:pl-28"
        ):
            # Left text
            with ui.column().classes("flex-1 gap-5"):
                ui.html(
                    f"""
                    <h2 style="
                        font-family:'Bebas Neue',sans-serif;
                        font-size:clamp(38px,5.5vw,66px);
                        line-height:1; letter-spacing:2px;
                        color:#f0e8d0; margin-bottom:4px;">
                      Your studio<br>deserves a badge<br>
                      of <span style="color:{C['gold_lt']}">distinction.</span>
                    </h2>
                """
                )
                ui.label(
                    "Studio managers: take the Bio CG Pledge and show clients, peers, "
                    "and the industry that in every frame your team delivers there is a testament "
                    "to genuine human skill and creative authorship."
                ).classes("max-w-md").style(
                    s(
                        font_size="16px",
                        line_height="1.7",
                        color="rgba(255,255,255,0.42)",
                    )
                )
                ui.button("Learn About the Pledge", on_click=lambda: None).props(
                    "outline no-caps"
                ).style(
                    s(
                        font_family="DM Mono, monospace",
                        font_size="11px",
                        letter_spacing="2px",
                        text_transform="uppercase",
                        color="rgba(255,255,255,0.55)",
                        border="1px solid rgba(255,255,255,0.15)",
                        background="rgba(255,255,255,0.06)",
                        border_radius="0",
                        padding="12px 28px",
                    )
                )

            # Pledge box card
            with (
                ui.card()
                .classes("w-full flex-1 md:w-96")
                .style(
                    s(
                        border="1px solid rgba(184,146,42,0.4)",
                        background="rgba(255,255,255,0.04)",
                        border_radius="0",
                        box_shadow="none",
                        position="relative",
                    )
                )
            ):
                ui.label("Bio CG Pledge").style(
                    s(
                        font_family="DM Mono, monospace",
                        font_size="9px",
                        letter_spacing="4px",
                        text_transform="uppercase",
                        color=C["gold"],
                        position="absolute",
                        top="-1px",
                        left="28px",
                        background=C["navy"],
                        padding="0 10px",
                        transform="translateY(-50%)",
                    )
                )
                with ui.card_section().classes(
                    "w-full p-10 md:p-11 gap-4 flex flex-col"
                ):
                    bebas_label(
                        "Take the Pledge",
                        size="28px",
                        color="#f0e8d0",
                        extra="display:block;margin-bottom:8px",
                    )
                    ui.label(
                        "Define your studio's commitment — Show off your score and member badge."
                    ).style(
                        s(
                            font_size="13px",
                            line_height="1.65",
                            color="rgba(255,255,255,0.38)",
                            display="block",
                            margin_bottom="28px",
                        )
                    )
                    ui.button("Engage Your Studio →", on_click=lambda: None).props(
                        "no-caps"
                    ).classes("w-full").style(
                        s(
                            font_family="DM Mono, monospace",
                            font_size="11px",
                            letter_spacing="2px",
                            text_transform="uppercase",
                            background=f"linear-gradient(135deg,{C['gold']},{C['gold_lt']})",
                            color=C["navy"],
                            border_radius="0",
                            font_weight="500",
                            padding="14px",
                        )
                    )


# ── STUDIOS ──────────────────────────────────────────────────────────────────


def build_studios():
    with (
        ui.element("section")
        .classes("w-full px-5 py-14 md:px-14 md:py-20 lg:pl-28")
        .style(
            s(
                background=C["bg"],
                border_bottom=f"1px solid {C['rule']}",
            )
        )
    ):

        # Header
        with (
            ui.row()
            .classes("items-baseline justify-between w-full mb-12")
            .style(
                s(
                    border_bottom=f"1px solid {C['rule']}",
                    padding_bottom="20px",
                )
            )
        ):
            bebas_label("Engaged Studios", size="44px")
            mono_label(
                "24 studios registered", size="10px", color=C["muted"], spacing="2px"
            )

        # Cards grid
        with ui.grid(columns=3).classes(
            "gap-4 w-full grid-cols-1 md:grid-cols-2 lg:grid-cols-3"
        ):
            for studio in STUDIOS:
                pill_color, pill_border, pill_bg = PILL_CFG[studio["pill"]]
                with (
                    ui.card()
                    .style(
                        s(
                            background=C["panel"],
                            border=f"1px solid {C['rule']}",
                            border_radius="0",
                            box_shadow="none",
                            position="relative",
                            overflow="hidden",
                            # transition="transform 0.25s, box-shadow 0.25s",
                            cursor="pointer",
                        )
                    )
                    .classes("transition duration-250 hover:scale-105 hover:z-10")
                ):
                    with ui.card_section().classes("p-7 gap-4 flex flex-col"):
                        # Name + score pill
                        with ui.row().classes(
                            "items-start justify-between gap-2 w-full"
                        ):
                            with ui.column().classes("gap-0"):
                                bebas_label(
                                    studio["name"], size="21px", extra="line-height:1.1"
                                )
                                mono_label(
                                    studio["location"],
                                    size="10px",
                                    color=C["muted"],
                                    spacing="1px",
                                    extra="margin-top:3px;display:block",
                                )
                            ui.label(studio["score"]).style(
                                s(
                                    font_family="Bebas Neue, sans-serif",
                                    font_size="14px",
                                    letter_spacing="1px",
                                    padding="4px 11px",
                                    border=f"1px solid {pill_border}",
                                    color=pill_color,
                                    background=pill_bg,
                                    white_space="nowrap",
                                    flex_shrink="0",
                                )
                            )

                        # Pledge badges
                        with ui.row().classes("gap-1 flex-wrap"):
                            for b in studio["badges"]:
                                pill_badge(b)

                        # Quote
                        ui.separator().style(f"border-color:{C['rule']}")
                        ui.label(f'"{studio["quote"]}"').style(
                            s(
                                font_size="12.5px",
                                font_style="italic",
                                line_height="1.65",
                                color=C["ink_mid"],
                                border_left=f"2px solid {C['rule']}",
                                padding_left="14px",
                            )
                        )

            # Empty slot
            with (
                ui.card()
                .classes(
                    "flex items-center justify-center cursor-pointer "
                    "hover:border-amber-400/60 hover:bg-amber-50/20 transition-all"
                )
                .style(
                    s(
                        border=f"1px dashed {C['rule']}",
                        background="transparent",
                        border_radius="0",
                        box_shadow="none",
                        min_height="220px",
                    )
                )
            ):
                with ui.column().classes(
                    "w-full h-full justify-center items-center gap-3"
                ) as c:
                    c.classes("transition duration-250 hover:scale-110 hover:z-10")

                    bebas_label("+", size="48px", color=C["rule"])
                    mono_label(
                        "Register Your Studio",
                        size="10px",
                        color=C["muted"],
                        spacing="3px",
                    )


# ── FOOTER ───────────────────────────────────────────────────────────────────


def build_footer():
    with (
        ui.element("footer")
        .style(
            s(
                background=C["navy"],
                position="relative",
                overflow="hidden",
                background_image=(
                    "repeating-linear-gradient(-45deg,"
                    "rgba(255,255,255,0.02) 0,rgba(255,255,255,0.02) 1px,"
                    "transparent 1px,transparent 14px)"
                ),
            )
        )
        .classes("w-full px-5 py-12 md:px-14 md:pt-16 md:pb-12 lg:pl-28")
    ):

        with ui.grid(columns=4).classes(
            "gap-8 mb-12 w-full grid-cols-2 md:grid-cols-4"
        ):
            # Brand
            with ui.column().classes("gap-3 col-span-2 md:col-span-1"):
                bebas_label(
                    "Bio CG",
                    size="28px",
                    color=C["gold_lt"],
                    spacing="4px",
                    extra="display:block",
                )
                ui.label(
                    "A global movement protecting the craft, career, and cultural "
                    "value of human-first computer graphics."
                ).style(
                    s(
                        font_size="13px",
                        line_height="1.65",
                        color="rgba(255,255,255,0.28)",
                        max_width="240px",
                    )
                )

            # Link columns
            for col_title, links in FOOTER_LINKS.items():
                with ui.column().classes("gap-2"):
                    mono_label(
                        col_title,
                        size="9px",
                        color=C["gold"],
                        spacing="3px",
                        extra=f"border-bottom:1px solid rgba(184,146,42,0.2);padding-bottom:12px;margin-bottom:6px;display:block",
                    )
                    for link in links:
                        ui.label(link).props("flat no-caps").on(
                            "click", lambda e: print(e)
                        ).classes(
                            "text-white/30 hover:text-amber-300 justify-start w-full cursor-pointer"
                        ).style(
                            s(
                                font_family="DM Sans, sans-serif",
                                font_size="13px",
                                font_weight="300",
                                # color="rgba(255,255,255,0.32)",
                                padding="2px 0",
                                min_height="unset",
                                text_align="left",
                            )
                        )

        ui.separator().style(f"border-color:rgba(184,146,42,0.15);margin-bottom:24px")

        with ui.row().classes("items-center justify-center flex-wrap gap-4 w-full"):
            mono_label(
                "© 2026 Bio CG — made with ❤︎ by tgzr.org",
                size="10px",
                color="rgba(255,255,255,0.2)",
                spacing="1px",
                upper=False,
            )
            with ui.row().classes("gap-6"):
                ui.image("/assets/by-sa.svg").classes("opacity-50 w-[6em]")


@ui.page("/")
def index():
    ui.add_head_html(HEAD_HTML)
    build_nav()
    with ui.column().classes("w-full gap-0").style(f"background:{C['bg']}"):
        build_hero()
        build_score_section()
        build_callout()
        build_studios()
        build_footer()
