--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2 (Debian 16.2-1.pgdg120+2)
-- Dumped by pg_dump version 16.2 (Debian 16.2-1.pgdg120+2)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	flights	city
8	flights	airline
9	flights	airport
10	flights	aggregator
11	flights	flight
12	flights	agg_flights
13	flights	historical_data
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add city	7	add_city
26	Can change city	7	change_city
27	Can delete city	7	delete_city
28	Can view city	7	view_city
29	Can add airline	8	add_airline
30	Can change airline	8	change_airline
31	Can delete airline	8	delete_airline
32	Can view airline	8	view_airline
33	Can add airport	9	add_airport
34	Can change airport	9	change_airport
35	Can delete airport	9	delete_airport
36	Can view airport	9	view_airport
37	Can add aggregator	10	add_aggregator
38	Can change aggregator	10	change_aggregator
39	Can delete aggregator	10	delete_aggregator
40	Can view aggregator	10	view_aggregator
41	Can add flight	11	add_flight
42	Can change flight	11	change_flight
43	Can delete flight	11	delete_flight
44	Can view flight	11	view_flight
45	Can add agg_ flights	12	add_agg_flights
46	Can change agg_ flights	12	change_agg_flights
47	Can delete agg_ flights	12	delete_agg_flights
48	Can view agg_ flights	12	view_agg_flights
49	Can add historical_ data	13	add_historical_data
50	Can change historical_ data	13	change_historical_data
51	Can delete historical_ data	13	delete_historical_data
52	Can view historical_ data	13	view_historical_data
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$600000$lTWcpHXqp9lJnzbwXxVlcr$QftUy1G4WFEqV2u6UpS/eaO24MKQQOcTsuUuhohk1AI=	\N	t	admin			unrdeaddrop@gmail.com	t	t	2024-05-05 09:56:29.867659+00
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2024-05-05 09:56:28.778232+00
2	auth	0001_initial	2024-05-05 09:56:28.889091+00
3	admin	0001_initial	2024-05-05 09:56:28.919453+00
4	admin	0002_logentry_remove_auto_add	2024-05-05 09:56:28.926858+00
5	admin	0003_logentry_add_action_flag_choices	2024-05-05 09:56:28.935648+00
6	contenttypes	0002_remove_content_type_name	2024-05-05 09:56:28.951253+00
7	auth	0002_alter_permission_name_max_length	2024-05-05 09:56:28.958984+00
8	auth	0003_alter_user_email_max_length	2024-05-05 09:56:28.966316+00
9	auth	0004_alter_user_username_opts	2024-05-05 09:56:28.973797+00
10	auth	0005_alter_user_last_login_null	2024-05-05 09:56:28.98107+00
11	auth	0006_require_contenttypes_0002	2024-05-05 09:56:28.98373+00
12	auth	0007_alter_validators_add_error_messages	2024-05-05 09:56:28.996287+00
13	auth	0008_alter_user_username_max_length	2024-05-05 09:56:29.008113+00
14	auth	0009_alter_user_last_name_max_length	2024-05-05 09:56:29.016418+00
15	auth	0010_alter_group_name_max_length	2024-05-05 09:56:29.025481+00
16	auth	0011_update_proxy_permissions	2024-05-05 09:56:29.03457+00
17	auth	0012_alter_user_first_name_max_length	2024-05-05 09:56:29.042164+00
18	sessions	0001_initial	2024-05-05 09:56:29.064537+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 52, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 13, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 18, true);


--
-- PostgreSQL database dump complete
--

