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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO admin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.auth_group ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO admin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.auth_group_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO admin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.auth_permission ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO admin;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO admin;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.auth_user_groups ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.auth_user ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO admin;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO admin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.django_admin_log ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO admin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.django_content_type ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO admin;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.django_migrations ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO admin;

--
-- Name: flights_aggflight; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.flights_aggflight (
    id uuid NOT NULL,
    aggregator_id uuid NOT NULL,
    flight_id uuid NOT NULL
);


ALTER TABLE public.flights_aggflight OWNER TO admin;

--
-- Name: flights_aggregator; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.flights_aggregator (
    id uuid NOT NULL,
    name text
);


ALTER TABLE public.flights_aggregator OWNER TO admin;

--
-- Name: flights_airline; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.flights_airline (
    iata_code character varying(2) NOT NULL,
    name text
);


ALTER TABLE public.flights_airline OWNER TO admin;

--
-- Name: flights_airport; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.flights_airport (
    iata_code character varying(3) NOT NULL,
    city_id character varying(6)
);


ALTER TABLE public.flights_airport OWNER TO admin;

--
-- Name: flights_airport_airline; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.flights_airport_airline (
    id bigint NOT NULL,
    airport_id character varying(3) NOT NULL,
    airline_id character varying(2) NOT NULL
);


ALTER TABLE public.flights_airport_airline OWNER TO admin;

--
-- Name: flights_airport_airline_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

ALTER TABLE public.flights_airport_airline ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.flights_airport_airline_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: flights_city; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.flights_city (
    code character varying(6) NOT NULL,
    name character varying(255)
);


ALTER TABLE public.flights_city OWNER TO admin;

--
-- Name: flights_flight; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.flights_flight (
    id uuid NOT NULL,
    min_cost integer NOT NULL,
    max_cost integer NOT NULL,
    avg_cost integer,
    airline_id character varying(2) NOT NULL,
    from_airport_id character varying(3) NOT NULL,
    to_airport_id character varying(3) NOT NULL,
    date_first_checked date,
    date_last_checked date,
    date_of_flight date,
    day_of_flight character varying(9) NOT NULL
);


ALTER TABLE public.flights_flight OWNER TO admin;

--
-- Name: flights_historicaldata; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.flights_historicaldata (
    id uuid NOT NULL,
    min_cost integer NOT NULL,
    max_cost integer NOT NULL,
    avg_cost integer,
    date_checked date,
    date_of_flight date,
    day_of_flight character varying(9) NOT NULL
);


ALTER TABLE public.flights_historicaldata OWNER TO admin;

--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: flights_aggflight flights_aggflight_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.flights_aggflight
    ADD CONSTRAINT flights_aggflight_pkey PRIMARY KEY (id);


--
-- Name: flights_aggregator flights_aggregator_name_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.flights_aggregator
    ADD CONSTRAINT flights_aggregator_name_key UNIQUE (name);


--
-- Name: flights_aggregator flights_aggregator_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.flights_aggregator
    ADD CONSTRAINT flights_aggregator_pkey PRIMARY KEY (id);


--
-- Name: flights_airline flights_airline_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.flights_airline
    ADD CONSTRAINT flights_airline_pkey PRIMARY KEY (iata_code);


--
-- Name: flights_airport_airline flights_airport_airline_airport_id_airline_id_133954a2_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.flights_airport_airline
    ADD CONSTRAINT flights_airport_airline_airport_id_airline_id_133954a2_uniq UNIQUE (airport_id, airline_id);


--
-- Name: flights_airport_airline flights_airport_airline_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.flights_airport_airline
    ADD CONSTRAINT flights_airport_airline_pkey PRIMARY KEY (id);


--
-- Name: flights_airport flights_airport_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.flights_airport
    ADD CONSTRAINT flights_airport_pkey PRIMARY KEY (iata_code);


--
-- Name: flights_city flights_city_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.flights_city
    ADD CONSTRAINT flights_city_pkey PRIMARY KEY (code);


--
-- Name: flights_flight flights_flight_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.flights_flight
    ADD CONSTRAINT flights_flight_pkey PRIMARY KEY (id);


--
-- Name: flights_historicaldata flights_historicaldata_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.flights_historicaldata
    ADD CONSTRAINT flights_historicaldata_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: flights_aggflight_aggregator_id_4483d2d4; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX flights_aggflight_aggregator_id_4483d2d4 ON public.flights_aggflight USING btree (aggregator_id);


--
-- Name: flights_aggflight_flight_id_e39362c6; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX flights_aggflight_flight_id_e39362c6 ON public.flights_aggflight USING btree (flight_id);


--
-- Name: flights_aggregator_name_09893f17_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX flights_aggregator_name_09893f17_like ON public.flights_aggregator USING btree (name text_pattern_ops);


--
-- Name: flights_airline_iata_code_fcddaf17_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX flights_airline_iata_code_fcddaf17_like ON public.flights_airline USING btree (iata_code varchar_pattern_ops);


--
-- Name: flights_airport_airline_airline_id_caca8d66; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX flights_airport_airline_airline_id_caca8d66 ON public.flights_airport_airline USING btree (airline_id);


--
-- Name: flights_airport_airline_airline_id_caca8d66_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX flights_airport_airline_airline_id_caca8d66_like ON public.flights_airport_airline USING btree (airline_id varchar_pattern_ops);


--
-- Name: flights_airport_airline_airport_id_d50c8488; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX flights_airport_airline_airport_id_d50c8488 ON public.flights_airport_airline USING btree (airport_id);


--
-- Name: flights_airport_airline_airport_id_d50c8488_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX flights_airport_airline_airport_id_d50c8488_like ON public.flights_airport_airline USING btree (airport_id varchar_pattern_ops);


--
-- Name: flights_airport_city_id_7c65c960; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX flights_airport_city_id_7c65c960 ON public.flights_airport USING btree (city_id);


--
-- Name: flights_airport_city_id_7c65c960_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX flights_airport_city_id_7c65c960_like ON public.flights_airport USING btree (city_id varchar_pattern_ops);


--
-- Name: flights_airport_iata_code_0ed17849_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX flights_airport_iata_code_0ed17849_like ON public.flights_airport USING btree (iata_code varchar_pattern_ops);


--
-- Name: flights_city_code_1e6cbfae_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX flights_city_code_1e6cbfae_like ON public.flights_city USING btree (code varchar_pattern_ops);


--
-- Name: flights_flight_airline_id_6abbe644; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX flights_flight_airline_id_6abbe644 ON public.flights_flight USING btree (airline_id);


--
-- Name: flights_flight_airline_id_6abbe644_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX flights_flight_airline_id_6abbe644_like ON public.flights_flight USING btree (airline_id varchar_pattern_ops);


--
-- Name: flights_flight_from_airport_id_2d9bae69; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX flights_flight_from_airport_id_2d9bae69 ON public.flights_flight USING btree (from_airport_id);


--
-- Name: flights_flight_from_airport_id_2d9bae69_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX flights_flight_from_airport_id_2d9bae69_like ON public.flights_flight USING btree (from_airport_id varchar_pattern_ops);


--
-- Name: flights_flight_to_airport_id_17993817; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX flights_flight_to_airport_id_17993817 ON public.flights_flight USING btree (to_airport_id);


--
-- Name: flights_flight_to_airport_id_17993817_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX flights_flight_to_airport_id_17993817_like ON public.flights_flight USING btree (to_airport_id varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: flights_aggflight flights_aggflight_aggregator_id_4483d2d4_fk_flights_a; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.flights_aggflight
    ADD CONSTRAINT flights_aggflight_aggregator_id_4483d2d4_fk_flights_a FOREIGN KEY (aggregator_id) REFERENCES public.flights_aggregator(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: flights_aggflight flights_aggflight_flight_id_e39362c6_fk_flights_flight_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.flights_aggflight
    ADD CONSTRAINT flights_aggflight_flight_id_e39362c6_fk_flights_flight_id FOREIGN KEY (flight_id) REFERENCES public.flights_flight(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: flights_airport_airline flights_airport_airl_airline_id_caca8d66_fk_flights_a; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.flights_airport_airline
    ADD CONSTRAINT flights_airport_airl_airline_id_caca8d66_fk_flights_a FOREIGN KEY (airline_id) REFERENCES public.flights_airline(iata_code) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: flights_airport_airline flights_airport_airl_airport_id_d50c8488_fk_flights_a; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.flights_airport_airline
    ADD CONSTRAINT flights_airport_airl_airport_id_d50c8488_fk_flights_a FOREIGN KEY (airport_id) REFERENCES public.flights_airport(iata_code) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: flights_airport flights_airport_city_id_7c65c960_fk_flights_city_code; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.flights_airport
    ADD CONSTRAINT flights_airport_city_id_7c65c960_fk_flights_city_code FOREIGN KEY (city_id) REFERENCES public.flights_city(code) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: flights_flight flights_flight_airline_id_6abbe644_fk_flights_airline_iata_code; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.flights_flight
    ADD CONSTRAINT flights_flight_airline_id_6abbe644_fk_flights_airline_iata_code FOREIGN KEY (airline_id) REFERENCES public.flights_airline(iata_code) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: flights_flight flights_flight_from_airport_id_2d9bae69_fk_flights_a; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.flights_flight
    ADD CONSTRAINT flights_flight_from_airport_id_2d9bae69_fk_flights_a FOREIGN KEY (from_airport_id) REFERENCES public.flights_airport(iata_code) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: flights_flight flights_flight_to_airport_id_17993817_fk_flights_a; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.flights_flight
    ADD CONSTRAINT flights_flight_to_airport_id_17993817_fk_flights_a FOREIGN KEY (to_airport_id) REFERENCES public.flights_airport(iata_code) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--
